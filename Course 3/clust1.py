import sys
from operator import itemgetter
class UnionFind(object):
    def __init__(self, n):
        self.graph = [0] * (n+1)
        self.len = [1] * (n+1)
        for i in range(n+1):
            self.graph[i] = i

    def union(self, n1, n2):
        p1 = self.parent(n1)
        p2 = self.parent(n2)
        self.graph[p1] = p2
            
        
    
    def parent(self, n1):
        p = self.graph[n1]
        if(p != n1):
            n1 = self.parent(p)
        return n1

def cluster():
    f=open('clust1.txt','r')
    x=f.readlines()

    uf = UnionFind(int(x[0]))
    e = []
    for line in x[1:] :
        line=line.split()
        
        val=[int(i) for i in line]
        e.append([val[0],val[1],val[2]])

    e = sorted(e, key = itemgetter(2))
    

    n = int(x[0])
    
    clusters = n
    for i in range(len(e)):
        n1, n2, cost = e[i]
        
        p1 = uf.parent(n1)
        p2 = uf.parent(n2)
        uf.union(n1, n2)
        np1 = uf.parent(n1)
        np2 = uf.parent(n2)
        
        if p1 != np1 or p2 != np2:
            clusters -= 1
            if clusters == 3:
                spacing = cost
                print(spacing)
                break
    
cluster()