def fib(n):
  global table
  if not table[n] and n>=0:
     if n<=1:
       table[n]=n
     else:
       table[n]=fib(n-1)+fib(n-2)
  return table[n]
        
if __name__=="__main__":
   table=[None]*100
   for i in range(0,10):
      print(fib(i))

   