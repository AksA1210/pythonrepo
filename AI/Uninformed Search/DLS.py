
WHITE=1
GREY=0
BLACK=-1

class Graph2:

  def __init__(self,M):
    self.Matrix=M
    self.N=M.shape[0]
    self.parent= [None for i in range(self.N)]
    self.color= [WHITE for i in range(self.N)]

  def getParent(self,index):
        return self.parent[index]

  def getColor(self,index):
      return self.color[index]
  
  def setParent(self,index,P):
      self.parent[index] = P
      
  def setColor(self,index,color):
      self.color[index] = color
      
  def getAdjacent(self,index):
      A=[]
      for i,v in enumerate(self.Matrix[index,:]):
          if v!=0:
              A.append(i)
      return A

class DLS:

  def __init__(self,Graph2,MaxD,goal):
    self.G=Graph2
    self.Path=[]
    self.D=MaxD
    self.level=1
    self.Goal=goal
  
  def Traversal(self,S):
    self.Path.append(S)
    self.G.setColor(S,BLACK)
    if S==self.Goal:
      return self.Path
    elif len(self.Path)==self.D:
      return False
    else:
      self.level=self.level+1
    for v in self.G.getAdjacent(S):
      if self.G.getColor(v) == WHITE:
        temp=self.Traversal(v)
        if temp==True:
          return self.Path
        elif temp==self.Path:
            return self.Path 
        else:
          self.Path.remove(v)
    return False  
          
    

import numpy as np
M = np.array([[0,1,1,1,0,0,0,0],
              [1,0,0,0,1,1,0,0],
              [1,0,0,0,0,0,1,1],
              [1,0,0,0,0,0,0,1],
              [0,1,0,0,0,1,0,0],
              [0,1,0,0,1,0,1,0],
              [0,0,1,0,0,1,0,0],
              [0,0,1,1,0,0,0,0]])


G = Graph2(M)
search = DLS(G,4,5)
print(search.Traversal(3))

Output : [3, 0, 1, 5]
