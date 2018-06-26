from scipy.spatial import distance
b=[]
a=[]
def euclidean(v1, v2):
    dist = distance.euclidean(v1, v2)
    return dist
def tsp(l,n):
    
    cost=0
    dist = [[euclidean(x,y) for y in l] for x in l]
    print(dist)
    for i in range(n):
        b.append(i)
    a=[0]
    sum=0
    while len(b)>=1:
        dmin = float("inf")
        for i in b:
            d = dist[a[-1]][i]
            if d < dmin:
                dmin = d
                c = i
        a.append(c)
        b.remove(c)
        sum+=dmin
    
    sum+=dist[a[-1]][0]
    return sum
f=open('nn.txt','r')
x=f.readlines()
n=int(x[0])
l=[]
for line in x[1:]:
    line = line.split()
    l.append([float(line[1]),float(line[2])])
m=tsp(l,n)
print(int(m))