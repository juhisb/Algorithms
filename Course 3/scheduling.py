  
from operator import itemgetter
import numpy as np
w=[]
l=[]

f=open('sch.txt','r')
x=f.readlines()
for line in x :
    line=line.split()
    
    if len(line) == 1:
        n=int(line[0])
        continue
        
    val=[int(i) for i in line]
    w.append(val[0])
    l.append(val[1])
diff=[[0]]*n
order=[]
diff1=[]
count=[]
diff3=[]
w1=[0]*n
for i in range(0,n):
    diff[i]=[i,(w[i]-l[i])]
diff=sorted(diff,key = itemgetter(1),reverse=True)

for i in range(0,n):
    w1[i]=w[diff[i][0]]
for i in range(0,n):
    diff1.append(diff[i][1])
diff2 =list(np.unique(np.array(diff1)))

for i in diff2:
    count.append([i,diff1.count(i)])

for i in range(len(diff2)):
    if count[i][1]>1:
        j=diff1.index(diff2[i])
        k=len(diff1) - diff1[::-1].index(diff2[i]) - 1
        
        diff[j:k+1]=[x for y,x in sorted(zip(w1[j:k+1],diff[j:k+1]),reverse=True)]
        if count[i][0] == 67:
            print(j,k,w1[j:k+1],diff[j:k+1])

        #diff3.append(diff)

diff=sorted(diff,key = itemgetter(1),reverse=True)



    
for i in range(0,n):
    order.append(diff[i][0])


time = 0
c=0
for i in order:
    c+=l[i]
    time+=w[i]*c
print(time)
            


    