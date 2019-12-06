class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dist=dist

def isinside(x,y,N):
    if x<0 or x>=N:
       return False
    if y<0 or y>=N:
       return False
    return True

def knight_tour(kpos,tpos,N):
    dx=[2,2,-2,-2,1,-1,1,-1]
    dy=[1,-1,1,-1,2,2,-2,-2]
    queue=[]
    queue.append(Cell(kpos[0],kpos[1],0))
    visited=[[False for i in range(N)] for i in range(N)]
    visited[kpos[0]][kpos[1]]=True
    while queue:
         m=queue.pop(0)
         if m.x==tpos[0] and m.y==tpos[1]:
            return m.dist
         for i in range(8):
            x=m.x+dx[i]
            y=m.y+dy[i]
            if isinside(x,y,N):
              if visited[x][y]==False:
                queue.append(Cell(x,y,m.dist+1))
                visited[x][y]=True

if __name__=="__main__":
   kpos=[2,3]
   tpos=[10,11]
   print(knight_tour(kpos,tpos,12))

   
   

    
    