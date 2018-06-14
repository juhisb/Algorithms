import sys, threading
from collections import defaultdict,Counter
sys.setrecursionlimit(2 ** 20)
threading.stack_size(67108864)
t=0
s=None
f=dict.fromkeys(range(875715), 0)
lead = [0]*875715
n=875715
 
#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list) 
    
    def addEdge(self,u,v):
        self.graph[u].append(v)  
    def getReverse(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def DFS1(self,i,explored):
        explored[i] = True
        global lead
       
        lead[i]=s
        global f
        stack = []
        stack.append(i)
        while stack:
            k=stack[-1]
            finished = True
            for j in self.graph[k]:
            
                if explored[j]== False:
                    explored[j]=True
                    stack.append(j)
                    finished = False
                    lead[j]=s
                    
            if finished and stack:
                k=stack.pop()
                global t
                t+=1
                f[k]=t
                
    def DFSLoop(self,explored):
        global t
        global s
        for i in range(n-1,1,-1):
            if explored[i] == False :
                
                
                s=i
                self.DFS1(i,explored)
    
    def DFSLoop1(self,i,explored):
        global t
        global s
    
        if explored[i] == False :
                
            
            s=i
            self.DFS1(i,explored)
    
    def computeSCC1(self):
        
        l=[0]*875715
        gr=self.getReverse()
        explored = dict.fromkeys(range(875715), False)
        #print(explored)
        gr.DFSLoop(explored)
        
        explored = dict.fromkeys(range(875715), False)
        #print(explored)

        #for i in range(0,n-1):
            #l[i]=f.index(max(f))
            #f[f.index(max(f))]=0
        
        for i in sorted(f,key = f.get,reverse=True):
            #print(i)
            if explored[i]==False:
                self.DFSLoop1(i,explored)
        return lead    

def main():
    g = Graph(875715)
    f=open('scc1.txt','r')
    x=f.readlines()
    for l in x :
        l=l.split()
    
        val=[int(i) for i in l]
    
    
        for j in range(1,len(val)):
            g.addEdge(val[0],val[j])


 
    
    q=g.computeSCC1()
    print(Counter(q).most_common(5))
thread = threading.Thread(target=main)
thread.start()