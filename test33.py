def fib(n):
   table=[None]*(n+1)
   for i in range(0,n+1):
      if i<=1:
         table[i]=i
      else:
         table[i]=table[i-1]+table[i-2]
   return table[n]

if __name__=="__main__":
   for i in range(0,13):
      print(fib(i))

