#!/usr/bin/env python2.7

#Simulate hybrid offspring between two genotypes in eigenstrat format.
#USAGE: python script.py > output

import numpy as np
import sys
#import pysam
#import sys
#import re

#file1=open("Parental1.geno", "r")
#file2=open("Parental2.geno", "r")
#output_file=open("offspring_file.geno","w")
#out=[]

file1=np.genfromtxt("parent1",  dtype='int', delimiter=1)
file2=np.genfromtxt("parent2",  dtype='int', delimiter=1)

#print(file1)
#print(file2)
#print()

n1=np.size(file1)
n2=np.size(file2)
if n1 != n2:
	sys.exit('n1 .not equal. n2')

for i1 in range(n1):
	x=9		# si no encontrara asignacion se queda con 9
	if file1[i1]==0 and file2[i1]==0:
		x=0
		print x
	if file1[i1]==2 and file2[i1]==2:
		x=2
		print x
	if file1[i1]==0 and file2[i1]==2:
		x=1
		print x			
	if file1[i1]==2 and file2[i1]==0:
		x=1
		print x
	if file1[i1]==1 and file2[i1]==1:
		a=np.random.randint(4, size=1)	#random entre {0,1,2,3}
		if a[0]==0:
			x=0
		if a[0]==1 or a[0]==2:
			x=1
		if a[0]==3:
			x=2
		print x
	k=file1[i1]+file2[i1]	# k=1 se consigue con 01 y 10 solo.
	if k==1:
		a=np.random.randint(2, size=1) #random entre {0,1}
		if a[0]==0:
			x=0
		if a[0]==1:
			x=1	
		print x
	k=file1[i1]+file2[i1]	# k=3 se consigue con 12 y 21 solo.
	if k==3:
		a=np.random.randint(2, size=1)	#random entre {0,1}
		if a[0]==0:
			x=1
		if a[0]==1:
			x=2	
		print x
	k=file1[i1]+file2[i1]	# k>=9 cuando uno o ambos parentales tienen missing data.
	if k>=9:
		x=9	
		print x
