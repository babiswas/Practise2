def kadane_algo(str1):
   current=str1[0]
   maxm=str1[0]
   for i in range(1,len(str1)):
      current=max(str1[i],maxm+str1[i])
      if current>maxm:
         maxm=current
   return maxm

if __name__=="__main__":
   l=[1,-1,2,2,-1,-3,-5,3,4,6]
   print(kadane_algo(l))

     
   