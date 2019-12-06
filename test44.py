class Cell:
    def __init__(self,x,dist):
        self.x=x
        self.dist=dist
def isinside(x,N):
    if x<0 or x>=N:
       return False
    return True
def  min_steps(kpos,arr):
     dx=[1,-1]
     visited=[False]*len(arr)
     queue=[]
     queue.append(Cell(kpos,0))
     visited[0]=True
     while queue:
         m=queue.pop(0)
         if m.x==len(arr)-1:
           return m.dist
         for i in range(0,2):
              x=m.x+dx[i]
              if isinside(x,len(l)):
                if not visited[x]:
                   queue.append(Cell(x,m.dist+1))
                   visited[x]=True
         indexes=[i for i,j in enumerate(arr) if arr[i]==arr[m.x]]
         for i in indexes:
                if not visited[i]:
                    queue.append(Cell(i,m.dist+1))
                    visited[i]=True

if __name__=="__main__":
   l=[0,1,2,3,4,5,6,7,5,4,3,6,0,1,2,3,4,5,7]
   N=len(l)
   print(min_steps(0,l))