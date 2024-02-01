#!/usr/bin/env python3

import numpy as np
import sys

MAX_FRAMES = int(sys.argv[2])	# completed 1000ns simulation should have 5,000 frames
sys_nm = sys.argv[1]

count_array = np.zeros(MAX_FRAMES,dtype=int)
peptides = ['OA','OB','OC','OD','OE','OF','OG','OH','OI','OJ','OK','OL','OM','ON','OO','OP','OQ','OR','OS','OT','OU','OV','OW','OX','OY','OZ','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN']

for p in peptides:
    #print("intra"+p+".dat")
    inFile = open("intra"+p+".dat", "r")    # Open input file stream
    inFile.readline()                       # Skip first (header line)
    
    for line in inFile:                   # iterate over each line of file
        #print(line.split()[1])
        frame = int(line.split()[0])-1    # get first col values (frame number)
        count = int(line.split()[1])      # get second col values (intra count for the given frame of current pep)
        count_array[frame] += count	  # sum intra counts for all 40 peptides

inFile.close()                            # close file stream

outFile = open(sys_nm+"_intra_all.dat",'w')       	# open output file stream
outFile.write("frame"+'\t'+"intra_count"+'\n')	# write header 

for i in range(MAX_FRAMES):			# iterate over count_array
    #print(i, count_array[i])			
    outFile.write(str(i)+'\t'+str(count_array[i])+'\n')	# write sum to a single file
outFile.close()						# close output file stream
