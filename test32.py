import sys
table=[None]*100
def fib(n):
  global table
  if n>=0:
    if not table[n]:
       if n<=1:
          table[n]=n
       else:
          table[n]=fib(n-1)+fib(n-2)
    return table[n]

if __name__=="__main__":
   for i in range(0,int(sys.argv[1])):
      print(fib(i))
