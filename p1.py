# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:06:23 2018

@author: Mrunal
"""
import random
import csv
def read_data(filename):
    with open(filename,"r")as csvfile:
        datareader=csv.reader(csvfile,delimiter=",")
        traindata=[]
        for row in datareader:
            traindata.append(row)
        return (traindata)

#function for finding maximally specific set 
def findS():
    dataarr=read_data('enjoysport.csv')
    h=['0','0','0','0','0','0']
    rows=len(dataarr)
    columns=7 #cols=lem(dataarr[0])
    for x in range (1,rows):
        t=dataarr[x]
    #    print(t)
        if t[columns-1]=='1':
            for y in range(0,columns-1):
                if h[y]==t[y]:
                    pass
                elif h[y]!=t[y] and h[y]=='0':
                    h[y]=t[y]
                elif h[y]!=t[y] and h[y]!='0':
                    h[y]='?'
            print(h)
    print("Maximally specific set \n <",end=' ')
    for i in range(0,len(h)):
        print(h[i],end=' ')
        if i!=(len(h)-1) :
            print(",", end='')
    print('>')
findS()