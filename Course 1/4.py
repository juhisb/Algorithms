from random import randint
import copy
from copy import deepcopy

vert=[]
edge=[]
f=open('txt.txt','r')
x=f.readlines()
for l in x :
    l=l.split()
    
    val=[int(i) for i in l]
    
    vert.append(val[0])
    for j in range(1,len(val)):
        edge.append([val[0],val[j]])

def kargerMinCut(vert,edge):
    while len(vert)>2:
        ran=randint(0,len(edge)-1)
        #print(edge)
        e1=edge[ran]
        v1=e1[0]
        v2=e1[1]
        
        vert.remove(v2)
        for e in edge:
            if e[1]==v2 or e[0]==v2:
                if e[1]==v2:
                    e[1]=v1
                else:
                    e[0]=v1
            else:
                continue
        newEdge=[]
        for e in edge:
            if(e[0]==e[1]):
                continue
            newEdge.append(e)
        edge=newEdge
    return len(edge)

minCut=kargerMinCut(deepcopy(vert),deepcopy(edge))
for i in range(0,100):
    min=kargerMinCut(deepcopy(vert),deepcopy(edge))
    if minCut>min:
        minCut=min
print(int(minCut/2))








