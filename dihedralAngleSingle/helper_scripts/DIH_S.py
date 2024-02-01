#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Manual style for plots
import sys
sys.path.append('../')
import style
from rama_plot import *

sys_nm=["pkG","pkA","pkL","pkkg",'pkka',"pkkl"]
dataA=[]
dataB=[]

for i in range(6):
	# LYS STRAND
	df = pd.read_csv(str(i)+"_A_"+sys_nm[i]+".csv")
	df = df.tail(30*400) # last 400fr = last 800ns
	df = df[df["res"]%6==0]
	df = df[df["phi"]!=0]
	df = df[df["psi"]!=0]
	fig = rama_plot(df["phi"],df["psi"],df["frame"],sys_nm[i]+" LYS Containing Chain",time_min=100,time_max=500,ns_fr=2)
	#plt.tight_layout()
	plt.savefig(str(i)+"_"+sys_nm[i]+'_LYS_S.png',dpi=600,bbox_inches="tight")
	#plt.show()
	
	# GLU STRAND
	df = pd.read_csv(str(i)+"_B_"+sys_nm[i]+".csv")
	df = df.tail(30*400)
	df = df[df["res"]%6==0]
	df = df[df["phi"]!=0]
	df = df[df["psi"]!=0]
	fig = rama_plot(df["phi"],df["psi"],df["frame"],sys_nm[i]+" GLU Containing Chain",time_min=100,time_max=500,ns_fr=2)
	#plt.tight_layout()
	plt.savefig(str(i)+"_"+sys_nm[i]+'_GLU_S.png',dpi=600,bbox_inches="tight")
	#plt.show()
	
	