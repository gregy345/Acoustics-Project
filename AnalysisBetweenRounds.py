import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import wave
import sys
from scipy.io.wavfile import read  # reading wav files
import math
import cmath
import pylab
from compareAperture import compareAperture
from SyntheticAperture import syntheticAperture
import os # for opeining files in loop #change working diectory, count files in directory
import glob # looping throught all files in folder

"""
Compare wave files from adjacent positions
Input:  start = the starting time of the sinal (seconds) 
		end = the end time of the sinal (seconds)  
		slow = the slow time of the sinal (seconds)  
		fast = the fast time of the sinal (1xP seconds)  
Output: energy difference between points
"""

def main():
	
	print "what is start time?"
	start = input()
	print "what is end time?"
	end = input()
	print "what is slow time?"
	slow = input()
	print "what is fast time?"
	fast = input()
	print "what is sample rate?"
	SampleRateRedux = input()  
	print "what is inital round?, r1, r2, ... r10 "
	inital = raw_input()  
	print "what is other round?, r1, r2, ... r10 "
	other = raw_input()  
	print "start position?, 1, 2, 3, ..."
	startPos = input()  
	print "end position?, 1, 2, 3, ..."
	endPos = input()  

	basepath = 'C:/Users/Greg/Documents/AcousticsWorkingFiles/StatisticalAcoustics/DataFolderFull'
	nbr = len([name for name in os.listdir(basepath) if os.path.isfile(os.path.join(basepath, name))])
	os.chdir('C:/Users/Greg/Documents/AcousticsWorkingFiles/StatisticalAcoustics/DataFolderFull')
	fillist =  os.listdir(basepath) 

	rounds = {
		'r1' : [k for k in fillist if 'r1' in k],
		'r2' : [k for k in fillist if 'r2' in k],
		'r3' : [k for k in fillist if 'r3' in k],
		'r4' : [k for k in fillist if 'r4' in k],
		'r5' : [k for k in fillist if 'r5' in k],
		'r6' : [k for k in fillist if 'r6' in k],
		'r7' : [k for k in fillist if 'r7' in k],
		'r8' : [k for k in fillist if 'r8' in k],
		'r9' : [k for k in fillist if 'r9' in k],
		'r10' : [k for k in fillist if 'r10' in k],
	}

	sub1 = rounds[inital]
	sub2 = rounds[other]

	print "the number of files in the full directory is: {0}".format(nbr)
	print 'the names of files in full directory are:'
	print fillist
	print 'the files in inital round are: {0}'.format(sub1)
	print 'the files in other round are: {0}'.format(sub2)

	for i in range(startPos-1, endPos):
		log1 = read(sub1[i])
		log2 = read(sub2[i])
		eMat, eAvg = compareAperture(start, end, slow, fast, SampleRateRedux, log1, log2)
		print "Energy difference between {0} and {1} is {2}".format(sub1[i], sub2[i], eAvg) 

if __name__ == '__main__':
	main()


	