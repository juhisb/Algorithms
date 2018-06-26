from scipy.spatial import distance
from itertools import combinations
def euclidean(v1, v2):
    dist = distance.euclidean(v1, v2)
    return dist
def tsp(l,n):
    
    cost=0
    dist = [[euclidean(x,y) for y in l] for x in l]
    print(dist)
    A = {(frozenset([0, x+1]), x+1): (dist, [0,x+1]) for x,dist in enumerate(dist[0][1:])}
    #print(A)
    for m in range(2, n):
        A1 = {}
        
        for s in [frozenset(C) | {0} for C in combinations(range(1, n), m)]:
            for j in s - {0}:
                A1[(s, j)] = min( [(A[(s-{j},k)][0] + dist[k][j], A[(s-{j},k)][1] + [j]) for k in s if k != 0 and k!=j])  
        A = A1
        #print(A)
    res = min([(A[d][0] + dist[0][d[1]], A[d][1]) for d in iter(A)])
    for i in range(len(res[1])):
        
        cost+=dist[res[1][i]][res[1][(i+1)%n]]
        
    return cost
f=open('tsp.txt','r')
x=f.readlines()
n=int(x[0])
l=[]
for line in x[1:]:
    line = line.split()
    l.append([float(line[0]),float(line[1])])
m=tsp(l,n)
print(int(m))