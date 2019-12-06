from collections import defaultdict

class Graph:
  def __init__(self,vertex):
      self.graph=defaultdict(list)
      self.vertex=vertex

  def add_edges(self,u,v):
       self.graph[u].append(v)

  def BFS(self,u,level):
      visited=[False]*self.vertex
      count=0
      queue=[]
      if level==1:
         print(u)
         return
      queue.append(u)
      visited[u]=True
      while queue:
        q_len=len(queue)
        while q_len:
           m=queue.pop(0)
           for i in self.graph[m]:
              if not visited[i]:
                 queue.append(i)
                 visited[i]=True
           q_len=q_len-1
        count=count+1
        if count==level:
           print(queue)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.BFS(2,3)


     