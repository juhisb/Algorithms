from operator import itemgetter
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
for i in range(0,n):
    diff[i]=[i,float(w[i]/l[i])]
diff =sorted(diff,key = itemgetter(1),reverse=True)
for i in range(0,n):
    order.append(diff[i][0])
for i in range(0,n-1):
    if diff[i][1]==diff[i+1][1]:
        if w[i+1]>w[i]:
            temp=order[i]
            order[i]=order[i+1]
            order[i+1]=temp


time = 0
c=0
for i in order:
    c+=l[i]
    time+=w[i]*c
print(time)
            


    