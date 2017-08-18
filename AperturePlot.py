import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import matplotlib.image as mpimg
import numpy as np
import wave
import sys
from scipy.io.wavfile import read
from scipy import fftpack, ndimage
import math
import cmath
#from SyntheticAperture import syntheticAperture
import pylab
import re   # needed for printing varible name
import inspect   # needed for printing varible name
#import inspect, re # needed for printing varible name

"""
Compute the synthetic appeture matrix
Input:  matrix to plot

Output: matrix of pressures (Px )
"""
def varname(p):
	for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
		m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
	if m:
		return m.group(1)

#if __name__ == '__main__':
#	spam = 42
#	print varname(spam)

def plotAperture(matrix): #, xAxis, yAxis, title):
	yes = 2
	emat = abs(matrix)
	plt.imshow(emat)
	#plt.matshow(emat)
	#plb.title('this plot is:'%(matrix))
	#plt.title('this plot is:'%(varname(yes)))
	#plt.title('this plot is:' varname(yes))
	#plt.title(text_escape(__matrix__))
	plt.colorbar(orientation ='horizontal')
	plt.show()
   


