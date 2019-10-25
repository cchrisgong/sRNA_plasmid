'''
a plotting routine that plots two variable with two different ranges against one variable
'''

#importing graphic packages

import os
import matplotlib.pyplot as plt
import matplotlib
from numpy import loadtxt as loadtxt

from parameters import *
from Vector import *

def plot(filepath, xname, plotname):
	# Read data from .dat file
	parx, maxbefore, maxafter, increase, fwhm = loadtxt(filepath, unpack=True)

	# Create a figure with size 6 x 6 inches.
	fig = plt.figure(figsize=(12,6))
    
	# Create the subplots.
	ax1 = fig.add_subplot(111)

	# Display Grid.
	ax1.grid(True,linestyle= '-',color= '0.75')
	ax1.plot(1e0, 8.6e0, 'r^',markersize=10)
	ax1.plot(1e0, 7.3e0, 'r^',markersize=10)
	# Generate the Scatter Plot
	ax1.plot(parx, increase, 'mo-')
	ymin, ymax = ax1.get_ylim()
	plt.axvline(e0, linewidth=2, color='r')
	
	# Set the X Axis label.
	#ax1.set_xlabel(xname, fontsize=12)

	# Set the Y Axis label.
	#ax1.set_ylabel('increase', color='m')
	#ax1.set_ylim(8.3,8.8) #(for pp)
	for tl in ax1.get_yticklabels():
    		tl.set_color('m')

	ax1.set_xticklabels(ax1.get_xticks(), fontsize = 20)
	ax1.set_yticklabels(ax1.get_yticks(), fontsize = 20)	
	
	ax1.set_xscale('log')
	ax1.set_xlim(0e0,1e0)
	
	# generate a parallel graph with y axis on the RHS
	ax2 = ax1.twinx()
	ax2.plot(parx, fwhm,'bo-')
	#ax2.set_ylim(46,51) #(for pp)
	#ax2.set_ylabel('fwhm', color='b')
	for tl in ax2.get_yticklabels():
	    tl.set_color('b')
	ax2.set_yticklabels(ax2.get_yticks(), fontsize = 20)
	ax2.set_xlim(0e0,1e0)	
	
	fig.savefig(plotname, dpi=500)

def plotloop(i):
	xname = partitles[i]
	plotname = parnames[i] + ".png"
	filename = parnames[i] + ".dat"
	plot(os.path.join("parscans", filename), xname, plotname)
	
if __name__ == "__main__":
	for i in range(2,3,1):
		plotloop(i)
