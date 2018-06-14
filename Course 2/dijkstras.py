vert=[]
def minDist(A):
    min = 1000000
    
    for v in vert:
        print(v)
        if A[v]<min and X[v] == False:
            min = A[v]
            min_index = v
    return min_index


l1=[0]*201

f=open('dij.txt','r')
x=f.readlines()
for line in x :
    l=[0]*201
    line=line.split()
    
    val=[str(i) for i in line]
    print(val)
    
    for j in range(1,len(val)):
        k=val[j].split(',')
        l[int(k[0])]=int(k[1])
    l1=l1+[l]
 
#print(l1)
for i in range(0,201):
    l1.remove(0)
    vert.append(i+1)
vert.remove(201)
V=dict.fromkeys(range(201), True)
X=dict.fromkeys(range(201), False)
X[0]=True
A=[1000000]*201
A[1]=0
while X!=V:
    v=minDist(A)
    #print(v)
    X[v]=True
    vert.remove(v)
    for w in vert:
        
        if l1[v-1][w] > 0 and X[w]==False and A[w] > A[v] + l1[v-1][w]:
            A[w] = A[v] + l1[v-1][w]
            
            #X[w] = True
            
print(A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197])
#7,37,59,82,99,115,133,165,188,197




    
    
