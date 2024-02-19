#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.ndimage.filters import gaussian_filter
from scipy.stats import kde

# Manual style for plots
import sys
sys.path.append('../')
import style
from PCA_emap import *

sys_nm=["pkG_peG","pkA_peA","pkL_peL","pkkg_peeg","pkka_peea","pkkl_peel"]

def get_range(df):
	range_val = int( max([abs(df['PC1'].min()), abs(df['PC2'].min()), abs(df['PC1'].max()), abs(df['PC2'].max())]) ) 
	print(range_val)
	return range_val

range_i=0
max_range=0
for i in range(6):
	df = pd.read_csv('data/'+sys_nm[i]+'/all_PCA_neg.csv')
	range_i = get_range(df)
	if(range_i > max_range):
		max_range = range_i
	
for i in range(6):
	plt.clf()
	df = pd.read_csv('data/'+sys_nm[i]+'/all_PCA_neg.csv')
	peak = find_peaks(df,200,max_range+15)
	print("peak:",peak)
	plot_PCA(df,sys_nm[i]+" GLU",200,max_range+15) #bins,range_val
	plt.scatter(peak[0],peak[1],marker='x', color='white')
	
	#plt.savefig(sys_nm[i]+"_PCS_P_neg.png",dpi=600,bbox_inches="tight")
	plt.show()
	
	plt.clf()
		
	df = pd.read_csv('data/'+sys_nm[i]+'/all_PCA_pos.csv')
	peak = find_peaks(df,200,max_range+15)
	print("peak:",peak)
	plot_PCA(df,sys_nm[i]+" LYS",200,max_range+15) #bins,range_val
	plt.scatter(peak[0],peak[1],marker='x', color='white')
	
	#plt.savefig(sys_nm[i]+"_PCS_P_pos.png",dpi=600,bbox_inches="tight")
	plt.show()
	