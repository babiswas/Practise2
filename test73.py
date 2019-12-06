def kadane_algo(arr):
   current=arr[0]
   maxm=arr[0]
   for i in range(0,len(arr)):
      curr=max(arr[i],current+arr[i])
      if curr>maxm:
         maxm=curr
   return maxm

if __name__=="__main__":
   print(kadane_algo([1,-1,12,11,-13,4]))
      
      