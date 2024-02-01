#pip install --upgrade pip setuptools wheel
#!pip install matplotlib

# standard imports:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def read_file( file_path ):
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line)
    return lines
    
# ("None"    0.000,"Ext"    1.000,"Bridge"    2.000,"3-10"    3.000,"Alpha"    4.000, "Pi"    5.000,"Turn"    6.000,"Bend"    7.000)
structure_types = ["None","Extended","Bridge","3-10","Alpha","Pi","Turn","Bend"]
frac = np.zeros(8)
count = np.zeros(8)
#500 2000 1750 4000 4000 5000
CONST_RES_NUM = 60
CONST_FRAME_NUM = int(float(sys.argv[1])) #5000
CONST_DELTA=0.001
count_matrix = np.zeros((CONST_RES_NUM+1,8))

lines = read_file(sys.argv[2])
    
## GET STRUCTURE COUNTS FOR EACH RESIDUE OVER ALL FRAMES
# count_matrix = np.zeros((61,8))
        
for line in lines:
    if line !='\n':
        res_id = int(''.join(list(line.split()[1])[:-4]))-1
        struct_type = int(line.split()[2])
        frame_num = int(''.join(list(line.split()[0])[:-4]))
        if(frame_num < CONST_FRAME_NUM+1):
            count_matrix[res_id,struct_type] += 1
            #print(res_id, struct_type)

## LOOK AT TOTAL COUNTS FOR EACH STRUCT TYPE
total_sum=0
for k in range(8):
    count[k]=sum(count_matrix[:CONST_RES_NUM,k])
    total_sum += sum(count_matrix[:CONST_RES_NUM,k])
    print("struct ",k,": ",count[k])
    #sanity check: grep '000             7' dssp.gnu | wc -l
    
if total_sum == CONST_RES_NUM*CONST_FRAME_NUM:
    print("\ntotal sum makes sense (",total_sum,")\n")
        
    ## DIVIDE BY #FRAMES and #residues:
for j in range(8):    
    print("struct ",j,": ",(sum(count_matrix[:CONST_RES_NUM,j]))/(CONST_RES_NUM*CONST_FRAME_NUM))
    frac[j]=sum(count_matrix[:CONST_RES_NUM,j])/(CONST_RES_NUM*CONST_FRAME_NUM)
            
print('\n')

s=0
for i in range(8):
    s+=frac[i]

if((s<1.0+CONST_DELTA)or(s>1.0+CONST_DELTA)):
	outFile = open(str(os.getcwd())+'/secstruct_frac.txt','w')
	for item in frac:
	    outFile.write("%s\n" % item)
	outFile.close()

	outFile = open(str(os.getcwd())+'/secstruct_count.txt','w')
	for item in count:
	    outFile.write("%s\n" % item)
	outFile.close()
	

	
