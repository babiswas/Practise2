def calculate_area(arr):
   arr=[str(i) for i in arr]
   str1=''.join(arr).split('0')
   str2=None
   max=0
   for i in str1:
     if len(i)>max:
        max=len(i)
        if len(i)>0:
          str2=[int(j) for j in list(i)]
   return min(str2)*len(str2)
   
#Histogram area technique.
def max_area_rectangle():
    M=[[1,0,0,1,1,1],[1,0,1,1,0,1],[0,1,1,1,1,1],[0,0,1,1,1,1]]
    max_area=0
    arr=[0]*len(M[0])
    for i in range(0,len(M)):
       for j in range(0,len(M[i])):
          if M[i][j]==0:
           arr[j]=0
          else:
           arr[j]=arr[j]+M[i][j]
       area=calculate_area(arr)
       if area>max_area:
         max_area=area
    return max_area


if __name__=="__main__":
    print(max_area_rectangle())

       
            
    