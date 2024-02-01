#!/usr/bin/python3
import numpy as np

def create_matrix(file_path="",dup_nm=""):
    val_matrix = np.zeros((30,30))
    #outFile = open("matrix"+dup_nm+".out","w")
    inFile = open(file_path)
    
    inFile.readline() # ignore header
    for line in inFile:
        #print(line)
        row=int(line.split()[0])-1
        col=int(line.split()[1])-1
        val=float(line.split()[2])
        val_matrix[row,col]=val
    #print(val_matrix)
    np.savetxt("matrix"+dup_nm+".out", val_matrix, delimiter=',',fmt='%1.4f')
    
def matrix_input(file_path,dup_nm=""):
    outFile = open("matrix_input_"+dup_nm+".out","w")
    inFile = open(file_path)
    inFile.readline()
    
    #print("Acceptor\tDoner\tFrames")
    outFile.write("Acceptor\tDoner\tFrac\n")
    for line in inFile:
        #Acceptor,Doner,Frames
        #print(line.split()[0],line.split()[1],line.split()[3])
        tmp = line.split()[0]
        offset1 = tmp.find('_')+1
        offset2 = tmp.find('@')
        #print(tmp[offset1]+tmp[offset2])
        acceptorId = str(int(tmp[offset1:offset2]))
        
        tmp = line.split()[1]
        offset1 = tmp.find('_')+1
        offset2 = tmp.find('@')
        #print(tmp[offset1]+tmp[offset2])
        donerId = str(int(tmp[offset1:offset2]))
        
        val = line.split()[4]
        
        #print(acceptorId+'\t'+donerId+'\t'+frameCount)
        outFile.write(acceptorId+'\t'+donerId+'\t'+val+'\n')
        
    inFile.close()
    outFile.close()

if __name__ == "__main__":
    matrix_input("pkA/intraOA_avgHbonds.dat",'pkA_A')
    #matrix_input("pkG/intraOA_avgHbonds.dat",'pkG_A')
    #matrix_input("pkL/intraOA_avgHbonds.dat",'pkL_A')
    #matrix_input("pkka/intraOA_avgHbonds.dat",'pkka_A')
    #matrix_input("pkkg/intraOA_avgHbonds.dat",'pkkg_A')
    #matrix_input("pkkl/intraOA_avgHbonds.dat",'pkkl_A')
    
    create_matrix("matrix_input_pkA_A.out","pkA_A")
    #create_matrix("matrix_input_pkG_A.out","pkG_A")
    #create_matrix("matrix_input_pkL_A.out","pkL_A")
    #create_matrix("matrix_input_pkka_A.out","pkka_A")
    #create_matrix("matrix_input_pkkg_A.out","pkkg_A")
    #create_matrix("matrix_input_pkkl_A.out","pkkl_A")
    

        