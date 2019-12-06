def max_area(M):
   max_area=0
   col=len(M[0])
   rows=len(M)
   arr=[0]*col
   for i in range(0,rows):
      for j in range(0,col):
         if M[i][j]==0:
            arr[j]=0
         else:
            arr[j]=arr[j]+M[i][j]
      area=calculate_area(arr)
      if area>max_area:
         max_area=area
   return max_area

def calculate_area(arr):
   arr=[str(i) for i in arr]
   str1=''.join(arr)
   str2=None
   max=0
   for i in str1.split('0'):
      if len(i)>max:
         max=len(i)
         str2=i
   str2=[int(i) for i in list(str2)]
   return min(str2)*len(str2)

if __name__=="__main__":
   M=[[1,0,0,1,1,1],[1,0,1,1,0,1],[0,1,1,1,1,1],[0,0,1,1,1,1]]
   print(max_area(M))


      
      

   

            
   