import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import wave
import sys
from scipy.io.wavfile import read
from scipy import fftpack, ndimage
import math 
import AperturePlot as ap
import re
 
"""
Compute the synthetic appeture matrix
	Input:  start = the starting time of the sinal (seconds) 
		end = the end time of the sinal (seconds)  
		slow = the slow time of the sinal (seconds)  
		fast = the fast time of the sinal (1xP seconds)  
		sound = wave file 
Output: matrix of pressures (NxP)
		matrix of fast fourier transform in both directions of pressures (NxP)
		matrix of log of fast fourier transform in both directions of pressures (NxP)
"""
def syntheticAperture(start, end, slow, fast, sound, SampleRateRedux):
	# the frequency will always be 44100 when using wave files 
	hz = 44100 
	samplerate = 44100/SampleRateRedux
	# convert varibles from seconds to indices in file
	iterations = int(float((end-start-fast)*(1/slow)))    
	#iterations = int(((end-start-fast)*(1/slow)))  
	StStart = int(float(start*samplerate))
	StSlow = int(float(slow*samplerate))
	StFast = int(float(fast*samplerate))

	# imports the wave file
	l = np.array(sound[1],dtype=float)
	b = l[0::SampleRateRedux]
	col3 = StFast
	cc = np.zeros((iterations, col3), dtype=complex)
	for j in range(0, iterations):
		for i in range(0, col3):
			cc[j,i] = b[i+(j*StSlow)] 
	fftt = fftpack.fft2(cc) 
	fftlog = np.array(np.log10(fftt), dtype=complex) 
	#ap.plotAperture(cc)
	return cc, fftt, fftlog
	#return cc, fftt, SampleRateRedux
	#return cc, fftt
"""	
# test data
#these are the varibles that will be input by user or program yet to be built
start = 0  # in seconds    2.91
end =  1   # in seconds   3.121   3.5 
slow = 0.0003  # in seconds    0.001   
fast = 0.2  # in seconds     0.05
SampleRateRedux = 4
# recorded wav file 
sound = read("audioFile1.wav") 

start = 0  # in seconds    2.91
end =  0.5   # in seconds   3.121   3.5 
slow = 0.0003  # in seconds    0.001   
fast = 0.2  # in seconds     0.05
SampleRateRedux = 4
# recorded wav file 
sound = read("audioFile1.wav") 

#syntheticAperture(start, end, slow, fast)
test = syntheticAperture(start, end, slow, fast, sound, SampleRateRedux)
print test

"""
