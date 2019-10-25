'''

This calculates the concentration of the components of the system: m, the amount of mRNA; s, the amount of sRNA; c, the amount of mRNA-sRNA compound; p, the amount of toxic protein. The data concentration data is then stored in a ascii file. The function also returns the protein level increase in terms of ratio and the fwhm of the protein increase peak after loss of plasmid.

var is a Vector containing m, s, c and p. The Vector class is defined in Vector.py.

'''
import os
import numpy
from numpy import loadtxt
from math import sqrt
import matplotlib.pyplot as plt

from Vector import *
from RK4 import *
from parameters import *
import singlerunplot

#def steadystates(parlistnew):
#	#(hminus + bc), bs, bm, bc, and bp could be zero
#	[g, pm, bm, ps, bs, hpl, hmi, bc, pp, bp] = parlistnew
#	if bc + hminus == 0: #simply accumulate complex
#	
#		return [s, m, c, p] #protein and complex may not be zero, here we only care about R (if p=0 R=1 by design), therefore it's a simplification
#	else:
#		if bc == 0:
#			
#		if bm == 0:
#			s = (ps-pm) * g / bs
#			m = (pm * g *(hminus + bc)) / (bc*hplus*s)
#			c = m * s * hplus / (hminus + bc)
#			p = pp * m / bp
#		else:
#			q = hplus - (hplus * hminus)/(hminus + bc)
#			star = (pm * g - ps * g) * q + bs * bm	
#			s = (sqrt(star ** 2e0 + 4e0 * q * bs * bm * ps * g) - star) / (2e0 * q * bs)
#			m = (pm * g + bs * s - ps * g) / bm
#			c = m * s * hplus / (hminus + bc)
#					
#			if bp ==0:
#				p = pp * m * 100e0
#			else:
#				p = pp * m / bp		
#	print p
#	return [s, m, c, p]
#		

def steadystates(parlistnew):
	[g, pm, bm, ps, bs, hplus, hminus, bc, pp, bp] = parlistnew
	q = hplus - (hplus * hminus)/(hminus + bc)

	star = (pm * g - ps * g) * q + bs * bm
	s = (sqrt(star ** 2e0 + 4e0 * q * bs * bm * ps * g) - star)/ (2e0 * q * bs)
	m = (pm * g - ps * g + bs * s) / bm
	c = m * s * hplus / (hminus + bc)
	p = pp * m / bp
	print [m, s, c, p]
	return [m, s, c, p]
	
def singlerun(parlistnew, filename, dirname):
	'''
	a function of number of integration steps, integration step size, filename
	'''
	[m0, s0, c0, p0] = steadystates(parlistnew)
	
	# initial values for [t, m, s, c, p]
	var = Vector([0., m0, s0, c0, p0])
	
	# to avoid the g set to 0 affect later scans
	parlistnew2 = []
	for s in parlistnew:
		parlistnew2.append(s)
	
	# treating negative components
	varcomponents = ["t", "m", "s", "m-s", "p"] #for tagging any negative component that needed to be restored to zero by hand

	# # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# # # 		main integration loop 		# # #
	flag = 0
	if p0 == 0:
		flag = 1
	
	if flag ==1:
		return p0, p0, 1e0, 0, flag
		
	p_old = p0
	decaytaglist = []	
	plist = []
	tlist = []
	for i in range(N):
		t = i * h
		tlist.append(t)
		
		# calls Runge-Kutta integration method
		var = RK4(var, t, parlistnew2)
        
        # set any computed concentration to zero if negative.
		for j in range(5):
			if var[j] < 0:
				print "negative concentration appears for " + varcomponents[j] + "!"
				var[j] = 0.
				
		p_new = var[-1]
		
		time_decay = 3 #deciding when to decide that the decaying behavior is not transient
		
		# early detection of a decaying solution
		if t < time_decay and p_new < p_old:
			decaytaglist.append(1)
			
		if t == time_decay and len(decaytaglist) == int(t/h):
			print "decaying soln"
			return p0, p0, 1e0, 0, flag #a decaying solution
			break
		
		#termination at half peak on the way down
		if i > 30 and p_new > p_old: #before the peak of a transient peak
			plist.append(p_new)
		
		if len(plist) != 0:
			print plist[-1], p_new
			if p_new < plist[-1]/2e0:
				t_b = t
				print t_b
				break
		
#		print i, p_new
		
		p_old = p_new
		
#	plt.plot(tlist[:len(plist)], plist)
#	plt.show()

	p_max = plist[-1]
	for p in plist:
		if p > p_max/2e0:
			i = plist.index(p)
			t_a = i* h
			break
			
	foldIncrease = p_max/p0
	fwhm = t_b - t_a
	print "concentration increased 100%: " + str(foldIncrease)
	print "protein peak width " + str(fwhm)		
	return p0, p_max, p_max/p0, fwhm, flag #a decaying solution	
	
if __name__ == "__main__":
	singlerun(defparlist, "singletrial", "")
