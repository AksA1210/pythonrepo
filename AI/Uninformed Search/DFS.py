
WHITE = 0
GREY = 1
BLACK = 2

class Graph:

  def __init__(self,M):
        self.Mat = M
        self.N = M.shape[0]
        self.parent = [None for _ in range(self.N)]
        self.color = [None for _ in range(self.N)]
  def getParent(self,index):
        return self.parent[index]
        
  def getColor(self,index):
        return self.color[index]
    
  def setParent(self,index,P):
        self.parent[index] = P
        
  def setColor(self,index,color):
        self.color[index] = color
        
  def getAdj(self, index):
        adj=[]
        for i,v in enumerate(self.Mat[index,:]):
            if v!=0:
                adj.append(i)
        return adj
    
class DFS:


  def __init__(self,G,source):

        self.G = G
        self.source = source
        self.Q = []
        self.result = []
  def traverse(self):
    
        for i in range(self.G.N):
            self.G.setColor(i,WHITE)
            self.G.setParent(i,None)
            
        self.Q.append(self.source)
        while self.Q :
            u = self.Q.pop(0)
            if self.G.getColor(u) == WHITE:
              self.G.setColor(u,GREY)
              self.visit(self.G,u)
            
  def visit(self,G,u):
    for v in self.G.getAdj(u):
      if self.G.getColor(v) == WHITE:
        self.G.setColor(v,GREY)
        self.G.setParent(v,u)
        self.visit(G,v)
    self.G.setColor(u,BLACK)
    self.result.append(u)

  def printResult(self):
        for u in self.result:
            print(u,end=' ')
        print('')
            
  def printLevel(self,curr,depth):
      if curr == None:
        return;
      for i in range(1,depth):
        print("│   ",end='')
      if depth > 0:
        print("|___",end='')
      print(curr);

      for child in [i for i,x in enumerate(self.G.parent) if x== curr]:
        self.printLevel(child, depth + 1);
        
             

import numpy as np

M = np.array([[0,1,1,0,0],
              [1,0,0,1,0],
              [1,0,0,1,1],
              [0,1,1,0,1],
              [0,0,1,1,0]])

G = Graph(M)
dfs = DFS(G,1)
dfs.traverse()
dfs.printResult()
dfs.printLevel(1,0)
        
