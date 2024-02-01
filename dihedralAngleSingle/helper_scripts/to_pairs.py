#!/usr/bin/env python
import sys
import pandas as pd

inFileName = sys.argv[1]
outFileName = sys.argv[2]
outFile=open(outFileName,'w')
outFile.write('frame,col,res,phi,psi\n')

with open(inFileName) as inFile:
    inFile.readline() # ignore first line (header)
    for line in inFile: # For each frame (line)
        frameNum = line.split()[0]  # get frame# (first col)
        maxVal = len(line.split())  # get max cols per line
        resId=0 # counter variable for loop below

        for i in range(1,maxVal+1,2):   # for each col per line, skipping every two cols (collecting pair values(i,i-1))
            if i == 1:  # If first col (first res) only PSI value possible
                #print(i,"psi")
                phi = 0
                psi = line.split()[1]
            elif i >= maxVal:   # Else if last col (last res) only PHI value possible
                #print(i,"phi")
                phi = line.split()[i-1]
                psi = 0
            else:
                phi = line.split()[i-1] # Else anything in between col1 and col max is a proper (PHI,PSI) pair value
                psi = line.split()[i]
                #print(i)
            
            resId +=1 # Increment counter variable to keep track of residue number for each PHI,PSI pair
            outFile.write(str(frameNum)+","+str(i)+","+str(resId)+","+str(phi)+","+str(psi)+"\n")

outFile.close()
