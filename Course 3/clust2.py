import sys,threading
from operator import itemgetter
sys.setrecursionlimit(2 ** 25)
threading.stack_size(67108864)
import gc
class UnionFind(object):
    def __init__(self, s):
        n=len(s)
        self.graph = dict.fromkeys(range(n))
        self.size = dict.fromkeys(range(n))
        for i in s:
            self.graph[i] = i
            self.size[i]=1

    def union(self, n1, n2):
        p1 = self.parent(n1)
        p2 = self.parent(n2)
        if self.size[p1] < self.size[p2]:
            self.graph[p1] = p2
            self.size[p2]+=self.size[p1]
        else:
            self.graph[p2] = p1
            self.size[p1]+=self.size[p2]

            
        
    
    def parent(self, n1):
        
        while (self.graph[n1] != n1):
            self.graph[n1] = self.graph[self.graph[n1]]
            n1=self.graph[n1]
        return n1


def invert(bit):
    if bit != '0' and bit != '1':
        raise ValueError
    return '1' if bit == '0' else '0'

def main():
    f=open('clustering_big.txt','r')
    x=f.readlines()


    s=set()
    for l in x[1:]:
        l=l.split()
        s.add(''.join(l))
    
    uf = UnionFind(s)
    l=x[0].split()
    n = int(l[0])
    b=int(l[1])
    print(len(s))
    clusters = len(s)
    count =1
    
    for i in s:
        print(count)
        for j in range(b):
            
            i1=i[:j]+invert(i[j]) + i[j+1:]
            if i1 in s:
                p1 = uf.parent(i)
                p2 = uf.parent(i1)
            
                uf.union(i, i1)
                np1 = uf.parent(i)
                np2 = uf.parent(i1)
        
                if p1 != np1 or p2 != np2:
                
                    clusters -= 1
        
        
        for j in range(b):
            for k in range(j+1, b):
                i2=i[:j]+invert(i[j])+i[j+1:k]+invert(i[k])+i[k+1:]
        
        
            
                
                if i2 in s:
                    p1 = uf.parent(i)
                    p2 = uf.parent(i2)
            
                    uf.union(i, i2)
                    np1 = uf.parent(i)
                    np2 = uf.parent(i2)
        
                    if p1 != np1 or p2 != np2:
                        clusters -= 1
            
        count+=1
        if count%10000 == 0:
            gc.collect()
    

    print(clusters)
thread = threading.Thread(target=main)
thread.start()




    
