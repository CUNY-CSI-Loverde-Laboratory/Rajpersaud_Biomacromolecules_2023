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


def cal_2d(x,y,temp,R,pmf_max,bin_val,r_val):
	
	H, xedges, yedges = np.histogram2d(x,y,density=True,bins=(bin_val,bin_val),range=([-1*r_val,r_val],[-1*r_val,r_val])) #[PC1,PC2] [x,y]
	
	stepx = xedges[1]-xedges[0]
	stepy = yedges[1]-yedges[0]
	xx, yy = np.mgrid[xedges.min():xedges.max():stepx,yedges.min():yedges.max():stepy]
	pos = np.dstack((xx, yy))
	
	pmax = 0
	for i in H:
		p = i.sum()
		if p >=pmax:
			pmax = p
	print("Found pmax = ",pmax)
	
	#Convert probabilities in H into energy values:
	for i in range(len(H)):
		for j in range(len(H.T)):
			if H[i,j]!=0:
				H[i,j]=-R*temp*np.log(H[i,j]/pmax)
			else:
				H[i,j]=pmf_max
				
	#print(" xedges, yedges, H = ",(H, xedges, yedges))
				
	return xedges,yedges,pos,H

def find_peaks(df,bins,range_val,e_max=2.4):
	
	df_len = df['PC1'].shape[0]
	x_mask=np.zeros(df_len)
	y_mask=np.zeros(df_len) # same length
	
	xedges,yedges,pos,H = cal_2d(df['PC1'],df['PC2'],310,0.001987,6.0,bins,range_val)
	peaks = np.argwhere(H <= e_max) # list pairs of H [x,y]. x and y are the computed heights, not indices!
	#print(peaks)
	
	while( (np.argwhere(H <= (e_max-0.1))).shape[0] !=0 ):
		e_max = e_max - 0.1
		peaks = np.argwhere(H <= e_max) 
	#outFile = open("find_peaks_"+name+"2.out", "w")
	
	for i in range(peaks.shape[0]):
		x_start = xedges[peaks[i][0]]
		x_end = xedges[peaks[i][0]+1]
		y_start = yedges[peaks[i][1]]
		y_end = yedges[peaks[i][1]+1]
		#print(peaks[i],x_start,x_end,y_start,y_end)
		j=0
		for each in df['PC1']:
			x_mask[j]=(each > x_start)&(each < x_end)
			j+=1
		j=0
		for each in df['PC2']:
			y_mask[j]=(each > y_start)&(each < y_end)
			j+=1
		
		x_mask = np.array(x_mask, dtype='bool')
		y_mask = np.array(y_mask, dtype='bool')
		mask = x_mask&y_mask
		#print(np.argwhere(mask == True))
		
		print(str(peaks[i])+','+str(x_start)+','+str(x_end)+','+str(y_start)+','+str(y_end))
	
	return ((x_start+x_end)/2,(y_start+y_end)/2)
	#	outFile.write(str(peaks[i])+','+str(x_start)+','+str(y_start)+','+str(x_end)+','+str(y_end))
		#for each in np.argwhere(mask == True):
		#	outFile.write(','+str(each))
		#outFile.write('\n')
	#outFile.close()
	
def find_min(df,name,bins,range_val):
	
	df_len = df['PC1'].shape[0]
	x_mask=np.zeros(df_len)
	y_mask=np.zeros(df_len) # same length
	
	xedges,yedges,pos,H = cal_2d(df['PC1'],df['PC2'],310,0.001987,6.0,bins,range_val)
	peaks = np.argwhere(H == H.min())
	
	outFile = open("find_min_"+name+".out", "w")
	
	for i in range(peaks.shape[0]): #peaks.shape[0]):
		x_start = xedges[peaks[i][0]]
		x_end = xedges[peaks[i][0]+1]
		y_start = yedges[peaks[i][1]]
		y_end = yedges[peaks[i][1]+1]
		#print(peaks[i],x_start,y_start, x_end,y_end)
	
		j=0
		for each in df['PC1']:
			x_mask[j]=(each > x_start)&(each < x_end)
			j+=1
		j=0
		for each in df['PC2']:
			y_mask[j]=(each > y_start)&(each < y_end)
			j+=1
			
		x_mask = np.array(x_mask, dtype='bool')
		y_mask = np.array(y_mask, dtype='bool')
		mask = x_mask&y_mask
		#print(np.argwhere(mask == True))
	
		outFile.write(str(peaks[i])+','+str(x_start)+','+str(x_end)+','+str(y_start)+','+str(y_end)+':')
		for each in np.argwhere(mask == True):
			outFile.write(','+str(each))
		outFile.write('\n')
	outFile.close()
	
def plot_PCA(df,name,bins,range_val):
	
	xedges, yedges,pos,H=cal_2d(df['PC1'],df['PC2'],310,0.001987,6.0,bins,range_val) ##
	smoothing_factor = 0.6
	H = gaussian_filter(H,smoothing_factor)
	plot = plt.contourf(pos[:,:,0],pos[:,:,1],H,extend='max',cmap='plasma')
	
	#plt.plot([3, 4], marker='*', ls='none', ms=5,color='green')
	
	plt.xlabel("Principal Component 1",fontsize=style.font_size)
	plt.ylabel("Principal Component 2",fontsize=style.font_size)
	plt.title(name)
	
	cbar = plt.colorbar(plot, pad = 0.01, aspect = 35)
	cbar.set_label('kcal/mol',rotation=90,labelpad=5,fontsize=style.font_size)
	cbar.ax.tick_params(labelsize=style.font_size)
	cbar.minorticks_on()
	
	plt.yticks(fontsize=style.font_size)
	plt.xticks(fontsize=style.font_size)