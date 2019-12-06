def max_rectangle(M):
    max_area=0
    row=len(M)
    col=len(M[0])
    arr=[0]*col
    for i in range(0,len(M)):
       for j in range(0,len(M[0])):
           if M[i][j]==0:
              arr[j]=0
           else:
              arr[j]=arr[j]+M[i][j]
       area=calculate_area(arr)
       if area>max_area:
          max_area=area
    return max_area

def calculate_area(arr):
    max_str=0
    str2=None
    arr=[str(i) for i in arr]
    str1=''.join(arr)
    str1=str1.split('0')
    for i in str1:
       if len(i)>=max_str:
          max_str=len(i)
          str2=i
    str2=[int(i) for i in str2]
    return min(str2)*len(str2)

if __name__=="__main__":
   M=[[1,0,0,1,1,1],[1,0,1,1,0,1],[0,1,1,1,1,1],[0,0,1,1,1,1]]
   print(max_rectangle(M))
   
   

          
    


           
   
     