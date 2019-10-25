'''
this code scans through one parameter value while holding all other nine parameters of the system of ODE fixed. Then plots the resulting scaled protein increase and its fwhm against this varying parameter. It utilizes the integrating loop written in singlerun.py which solves the ode as well as a parameter scanning loop written in parscanner function. 

'''
from parameters import *
from singlerun_an import *
from numpy import exp, log

def multiplerun(i):
	'''includes looping through the list of ten parameters, looping through the parameter range and integrating the system'''

	defparlist = [g, pm, bm, ps, bs, hplus, hminus, bc, pp, bp]

	pardirpath = os.path.join(os.getcwd(), "parscans") 
	try:
		os.makedirs(pardirpath)
	except OSError:
		pass # already exists

	parlistnew = []
	for l in defparlist:
		parlistnew.append(l) # make a copy of parameter list

#	parfilename = parnames[i] + "_fastequil_20_2e-1.dat"
#	parfilename = parnames[i] + "_fastequil_1e3_1e1.dat"
	parfilename = parnames[i] + "bc=bm.dat"
	parfilepath = os.path.join(pardirpath, parfilename)
	
	
	# incremented parameters (x-coordinates)
	xlst = [] 
	if i in [1,2,5,6]:
		rangeint = 50
		for k in range(rangeint)[22:]:
			xd = exp((log(range_endlist[i])/float(rangeint)) * k)-1

			xlst.append(range_startlist[i] + xd)
	else:
		res = resolution[i]
		rangeint = int((range_endlist[i] - range_startlist[i]) / res)
		for k in range(rangeint):
			xlst.append(res * k + range_startlist[i])
#	print xlst
	datadirname = parnames[i] 
	
	for j in xlst:
		FILE2 = open(parfilepath,'a')
		datafilename = parnames[i] + "=" + str(j) # file name like "g = 10" for the varied parameter g
		parlistnew[i] = j
		print parlistnew
		print j

		#change 0 to 1 for singlerunplot
		maxbefore, maxafter, increase, fwhm, footnote = singlerun(parlistnew, datafilename, datadirname) 
		dirpath = os.path.join(os.getcwd(), datadirname)
		print "maxafter", maxafter
		
		FILE2.write(str(j) + ' ' + str(maxbefore) + ' ' + str(maxafter) + ' ' + str(increase) + ' '+ str(fwhm) + '\n')
		FILE2.close()

if __name__ == "__main__":
#	for i in range(2):
#		multiplerun(i+9)
	multiplerun(1)
	#[g  , pm, bm, ps, bs, hpl,hmi,  bc,  pp, bp]
