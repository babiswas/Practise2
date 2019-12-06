def fib(n):
  mem=[None]*n
  if n>=0:
     if n<2 and n-1>=0:
        mem[n-1]=n
     else:
        if not mem[n-1]:
           if not mem[n-2]:
              mem[n-1]=fib(n-2)+fib(n-3)
           else:
              mem[n-1]=mem[n-2]+mem[n-3]
     
     return mem[n-1]

if __name__=="__main__":
   fib(4)

     