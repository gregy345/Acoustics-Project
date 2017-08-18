import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import wave
import sys
from scipy.io.wavfile import read
from scipy import fftpack, ndimage
import math
import cmath
from SyntheticAperture import syntheticAperture
import pylab
from AperturePlot import plotAperture
#from confusionMatrix import conMat

"""
Compute the synthetic appeture matrix
Input:  start = the starting time of the sinal (seconds) 
		end = the end time of the sinal (seconds)  
		slow = the slow time of the sinal (seconds)  
		fast = the fast time of the sinal (1xP seconds)  
	sound1 = simulated wave file
	sound2 = real world wave file 
Output: matrix of pressures (Px )
"""
def compareAperture(start, end, slow, fast, SampleRateRedux, sound1, sound2):

	cc1, fftt1, fftlog1 = syntheticAperture(start, end, slow, fast, sound1, SampleRateRedux)
	cc2, fftt2, fftlog2 = syntheticAperture(start, end, slow, fast, sound2, SampleRateRedux)

	row1 = fftt1.shape[0] 
	col1 = fftt1.shape[1]
	row2 = fftt2.shape[0]
	col2 = fftt2.shape[1]

	#energyMat = np.zeros((row1,col1), dtype=float)
	energyMat = np.zeros((row1,col1), dtype=complex)
	for i in range(0, row1):	
		for j in range(0, col1):
			energyMat[i,j] = 20*(np.log10(np.linalg.norm(fftt1[i,j]))-np.log10(np.linalg.norm(fftt2[i,j])))
	#return energyMat #, cc1
	#emat = abs(energyMat)
	#print fftt1
	#print fftt2
	print energyMat 
	print "this is the average of the decibel level differences"
	print np.average(energyMat)
	#plotAperture(fftlog1)
	#plotAperture(fftlog2)
	#plotAperture(energyMat)
	#conMat(cc1,cc2)

# test data
#these are the varibles that will be input by user or program yet to be built
start = 0  # in seconds    2.91
end =  0.5   # in seconds   3.121   3.5 
slow = 0.0003  # in seconds    0.001   
fast = 0.2  # in seconds     0.05
SampleRateRedux = 4

# recorded wav file 
sound1 = read("audioFile1.wav") 
sound2 = read("audioFile2.wav") 

#syntheticAperture(start, end, slow, fast)
print compareAperture(start, end, slow, fast, SampleRateRedux, sound1, sound2)

