from parameters import h
from Vector import *

'''
system of ODEs and RK4 integration method

'''

def RK4(var, t, parlistnew):
	
	'''algorithm function of RungeKutta of 4th order, input the initial vector var, 
	outputs the new vector var, t is the initial time, h the time step. 
	var, k1 to k4 are all 5-Vector containing [t, x, y, vx, vy]'''
	
	k1 = h * ode(var, t, parlistnew)
	k2 = h * ode(var + k1 / 2., t + h / 2., parlistnew)
	k3 = h * ode(var + k2 / 2., t + h / 2., parlistnew)
	k4 = h * ode(var + k3, t + h, parlistnew)
	
	var = var + (k1 + 2. * k2 + 2. * k3 + k4) / 6.	
	
	return var
	
def ode(var, t, parlistnew):
	
	# parlistnew is the list of parameters generated in multiplerun.py 
	# [g, pm, bm, ps, bs, hplus, hminus, bc, pp, bp]
	# input vector = var = Vector([t, m, s, c, p]) 
	m = var[1]
	s = var[2]
	c = var[3]
	p = var[4]

	# output vector = time derivative of input vector = deriv = Vector([dt, dm, ds, dc, dp])
	dt = 1. # don't have to propagate t here since it's already done in the main loop, but for convenience. No double propagation though.
	dm = - parlistnew[2] * m - parlistnew[5] * m * s + parlistnew[6] * c
	ds = - parlistnew[4] * s - parlistnew[5] * m * s + parlistnew[6] * c
	dc = parlistnew[5] * m * s - parlistnew[6] * c - parlistnew[7] * c
	dp = parlistnew[8] * m - parlistnew[9] * p

	#dm = pm * g - bm * m - hplus * m * s + hminus * c
	#ds = ps * g - bs * s - hplus * m * s + hminus * c
	#dc = hplus * m * s - hminus * c - bc * c
	#dp = pp * m - bp * p

	deriv = Vector([dt, dm, ds, dc, dp])

	return deriv
