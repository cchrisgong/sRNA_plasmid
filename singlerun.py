'''

This calculates the concentration of the components of the system: m, the amount of mRNA; s, the amount of sRNA; c, the amount of mRNA-sRNA compound; p, the amount of toxic protein. The data concentration data is then stored in a ascii file. The function also returns the protein level increase in terms of ratio and the fwhm of the protein increase peak after loss of plasmid.

var is a Vector containing m, s, c and p. The Vector class is defined in Vector.py.

'''
import os
import numpy
from numpy import loadtxt

from Vector import *
from RK4 import *
from parameters import N, h, tbreak
import singlerunplot

def singlerun(parlistnew, filename, dirname):
	'''
	a function of number of integration steps, integration step size, filename
	'''

	# initial values for [t, m, s, c, p]
	var = Vector([0., 0., 0., 0., 0.])

	# make a copy of parameter list for plotting purposes because we are otherwise g will be set to 0 at tbreak
	parlistplot = []
	for i in parlistnew:
		parlistplot.append(i) 
	
	# to avoid the g set to 0 affect later scans
	parlistnew2 = []
	for s in parlistnew:
		parlistnew2.append(s)

	# writing integrated dynamics data stored in corresponding folder that is created
	dirpath = os.path.join(os.getcwd(), dirname) 
	try:
		os.makedirs(dirpath)
	except OSError:
		pass # already exists
	filenamedat = filename + ".dat"
	filepath = os.path.join(dirpath, filenamedat)
	FILE = open(filepath,'w')
	
	# treating negative components
	varcomponents = ["t", "m", "s", "m-s", "p"] #for tagging any negative component that needed to be restored to zero by hand
	note = ["", "", "", "", ""]
	counter = [0, 0, 0, 0, 0] #for tagging how many times any component needed to be restored to zero

	# # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# # # 		main integration loop 		# # #

	for i in range(N):
        	t = i * h
		
		# set gene copy to be zero after l.o.p
		if t > tbreak:
			parlistnew2[0] = 0.

		# calls Runge-Kutta integration method
        	var = RK4(var, t, parlistnew2) 

		# set any computed concentation to zero if negative.
		for i in range(5):
			if var[i] < 0:
				var[i] = 0.
				note[i] = varcomponents[i]
				counter[i] +=1

		#writes t, m, s, c, p into data file
		FILE.write(str(var[0]) + ' ' + str(var[1]) + ' '+ str(var[2]) + ' '+ str(var[3]) + ' '+ str(var[4]) + ' ' + '\n')
    	FILE.close()	

	# # # 		end of main integration loop 	# # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # 

	# print a note on what component went negative at some point and how many times it had to be reset to zero
	noteprint = ""
	for i in range(len(note)):
		if note[i] != "":
			noteprint = noteprint + note[i] + "<0 x " + str(counter[i]) + "  "

	# compute the features of the system
	maxbefore, maxafter, increase, fwhm, flag = features(filepath, dirname)

	return maxbefore, maxafter, increase, fwhm, flag
	
def features(filepath, dirname):
	# get data
	t, m, s, c, p = numpy.loadtxt(filepath, unpack=True)

	# split the protein concentration data into before and after l.o.p
	p = p.tolist() # convert ndarray object into list
	plistbefore = p[ : int(tbreak / h) + 1]
	plistafter = p[int(tbreak / h) + 1 : ]

	# gives the peaks of protein before and after l.o.p and ratio of protein increase
	maxbefore = max(plistbefore)
	maxafter = max(plistafter)
	
	flag = 0 # flags when protein remains at a constant zero
	
	#### ratio of the protein concentration before and after l.o.p, set to 0 if the max of prot. conc. before l.o.p is zero constant
	if maxbefore == 0:
		flag = 1
		increase = 0
	else:
		increase = maxafter / maxbefore

	rightp, leftp = fwhmax(plistafter, maxafter)
	
	fwhm = (rightp-leftp) * h

	return maxbefore, maxafter, increase, fwhm, flag

def fwhmax(plistafter, maxafter):

	### full width at half max of the protein peak after loss of plasmids in units of minutes
	halfmax = maxafter / 2.
	if halfmax == 0:
		return 0, 0

	# from the the list of concentration after l.o.p. search the half max from the left.
	for k in plistafter:
		if k > halfmax:
			leftp = plistafter.index(k)
			break

	# reverse the list of concentration after l.o.p. to search the half max from the right.
	reversedplistafter = reversed(plistafter)
	for j in reversedplistafter:
		if j > halfmax:
			rightp = plistafter.index(j)
			break

	return rightp, leftp
