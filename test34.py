table=["NIL"]*100

def fib(n):
   global table
   if table[n]=="NIL":
      if n<=1:
         table[n]=n
      else:
         table[n]=fib(n-1)+fib(n-2)
   return table[n]

if __name__=="__main__":
   for i in range(0,10):
      print(fib(i))



