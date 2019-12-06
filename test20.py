from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def isCyclic_util(self,visited,u,recstack):
       visited[u]=True
       recstack[u]=True
       for i in self.graph[u]:
          if not visited[i]:
              if self.isCyclic_util(visited,i,recstack):
                 return True
          elif i in recstack:
                 return True
       recstack[u]=False
       return False
       

   def isCyclic(self):
      visited=[False]*self.vertex
      recstack=[False]*self.vertex
      for i in range(self.vertex):
        if not visited[i]:
           if self.isCyclic_util(visited,i,recstack):
              return True
      return  False

if __name__=="__main__":
   graph=Graph(8)
   graph.add_edges(0,1)
   graph.add_edges(0,3)
   graph.add_edges(3,2)
   graph.add_edges(3,4)
   graph.add_edges(4,5)
   graph.add_edges(4,6)
   graph.add_edges(4,7)
   print(graph.isCyclic())

   
   
   
 
               
             
