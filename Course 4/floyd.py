  
f=open('g3.txt','r')
x=f.readlines()
x1=x[0].split()
n=int(x1[0])
m=int(x1[1])
l=[[float("inf") for x in range(n+1)] for y in range(n+1)]
for line in x[1:]:
    line = line.split()
    l[int(line[0])][int(line[1])]=int(line[2])
for i in range(0,n+1):
    l[i][i] = 0

print(l)
d=[[0 for i in range(n+1)]for j in range(n+1)]
for i in range(n):
    for j in range(n):
        d[i][j] = l[i][j]
      
for k in range(1,n):
     
    for i in range(1,n):
            
        for j in range(1,n):
         
            
            d[i][j] = min(d[i][k] + d[k][j], d[i][j])
            #print(i,j,d[i][j])

  
  
for i in range(1,n+1):
    if (d[i][i] < 0):
        print("negative cycle")
        break

m = min([min(r) for r in d])   
print(m)

    



 