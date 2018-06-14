g=[]
f=open('edges.txt','r')
x=f.readlines()
for line in x :
    line=line.split()
    
    if len(line) == 2:
        n=int(line[0])
        e=int(line[1])
        continue
        
    val=[int(i) for i in line]
    g.append([val[0],val[1],val[2]])

adj = []
for i in range(0, n+1):
    adj.append([])
    for j in range(0, n+1):
        adj[i].append(0)

for i in range(0, len(g)):
    adj[g[i][0]][g[i][1]] = g[i][2]
    adj[g[i][1]][g[i][0]] = g[i][2]

vert = 1
T=[]
E=[]
explored = []
min = [None,None,float('inf')]
while len(T) != n-1:
    explored.append(vert)
    for r in range(1, n+1):
            if adj[vert][r] != 0:
                E.append([vert,r,adj[vert][r]])
    for e in range(0, len(E)):
        if E[e][2] < min[2] and E[e][1] not in explored:
            min = E[e]
    E.remove(min)
    T.append(min)
    vert = min[1]
    min = [None,None,float('inf')]

cost = 0
for i in range(0,n-1):
    cost+=T[i][2]
print(cost)

