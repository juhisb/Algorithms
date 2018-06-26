import gc
import sys
import threading

from collections import defaultdict
sys.setrecursionlimit(2 ** 20)
threading.stack_size(67108864)
t = 0
s = None
n = 0
explored = None
leader = None
lead = None
q = None
f = None

class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list) 
    
    def addEdge(self,u,j):
        self.graph[u].append(j)  
    def getReverse(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def DFS_Loop_1(self, n):
    
        global t, explored, f
    
        t = 0
        explored = [False]*n
        f = [None]*n
    
        for i in reversed(range(n)):
            if not explored[i]:
                self.DFS_1(i)
         
    def DFS_1(self, i):
    
        global t, explored
    
        explored[i] = True
    
        for j in self.graph[i]:
            #print(j)
            if not explored[j]:
                self.DFS_1(j)
    
        f[t] = i
        t += 1
    
    def DFS_Loop_2(self):
    
        global lead, explored, q, f
    
        explored = [False]*(2*n+1)
    
        for i in reversed(range(2*n+1)):
            if not explored[f[i]]:
                lead = set()
                q = False
                self.DFS_2(f[i])
                if q: break
            
        return q
    
    def DFS_2(self, i):
    
        global explored, lead, q
    
        explored[i] = True
        lead.add(i)
    
        if i < n:
            if (i+n) in lead:
                q = True
        elif (i-n) in lead:
            q = True
    
        for j in self.graph[i]:
            if not explored[j]:
                self.DFS_2(j)
    

    def computeSCC(self):
    
        gr=self.getReverse()
        #print(len(self.graph))
        gr.DFS_Loop_1(2*n+1)
        q = self.DFS_Loop_2()
    
        return q


def negate(a):
    if a<0:
        a=n-a
    
    
    return a
def main():

    global n

    for i in range(1, 7):
        
        f = open('2sat%i.txt' % i)
        x=f.readlines()
        n = int(x[0])
        
        
        g = Graph(n)
        for l in x[1:] :
            l=l.split()
    
            val=[int(i) for i in l]
    
    
            for j in range(1,len(val)):
           
                g.addEdge(negate(-val[0]),negate(val[j]))
                g.addEdge(negate(-val[j]),negate(val[0]))
        
        #g.addEdge(negate(-val[0]),negate(val[j]))
        #g.addEdge(negate(-val[j]),negate(val[0]))
        q = g.computeSCC()
        if q:
            print("0")  
        else:
             print("1")
        
        
        
        gc.collect()


thread = threading.Thread(target=main)
thread.start()
