'''
a plotting routine that plots four variable
'''

#importing graphic packages

import os
import matplotlib.pyplot as plt
from numpy import loadtxt as loadtxt

from Vector import *
from parameters import N, h

def plot(filepath, plotitle, xname, dirname, plotname):
	# Read data from .dat file
	t, m, s, c, p = loadtxt(filepath, unpack=True)

	# Create a figure with size 6 x 6 inches.
	fig = plt.figure(figsize=(12,6))
    
	# Create the subplots.
	ax = fig.add_subplot(111)

	# Set the title.
	ax.set_title(plotitle, fontsize=14)

	# Set the X Axis label.
	ax.set_xlabel(xname,fontsize=12)

	# Display Grid.
	ax.grid(True,linestyle= '-',color= '0.75')

	# Generate the Scatter Plot.
	p1 = ax.scatter(t, m, s=10, color= 'orange')
	p2 = ax.scatter(t, s, s=10, color= 'blue')
	p3 = ax.scatter(t, c, s=10, color= 'red')
	p4 = ax.scatter(t, p, s=10, color= 'green')

	#generate legend
	fig.legend((p1, p2, p3, p4), ("mRNA", "sRNA","mRNA-sRNA complex", "protein"), 'upper right', prop={'size':12})
	
#	xpos = N * h * 1.05
#	ypos = Vector(range(0,11)) * ax.axis()[3] * 0.7 / 11.

#	ax.text(xpos, ypos[10], noteprint, color='black', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[9], "genecopy = " + str(params[0]), color='purple', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[8], "prodrate_mRNA = " + str(params[1]), color='orange', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[7], "degrate_mRNA = " + str(params[2]), color='orange', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[6], "prodrate_sRNA = " + str(params[3]), color='blue', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[5], "degrate_sRNA = " + str(params[4]), color='blue', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[4], "bindingrate = " + str(params[5]), color='red', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[3], "unbindingrate = " + str(params[6]), color='red', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[2], "degrate_complex = " + str(params[7]), color='red', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[1], "prodrate_p = " + str(params[8]), color='green', fontsize=10, fontweight='bold')
#	ax.text(xpos, ypos[0], "degrate_p = " + str(params[9]), color='green', fontsize=10, fontweight='bold')

	# Save the generated Scatter Plot to a PNG file.
	fig.savefig(os.path.join(os.getcwd(), dirname, plotname), dpi=500)

if __name__ == "__main__":
	plot("g=1.0.dat", "", "", "", "singleplot.png")
