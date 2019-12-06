class A:
  def __init__(self,func):
     self.func=func
  def __call__(self,*args):
     print("Magic method call executed")
     return self.func(*args)


@A
def fun(*args):
  for i in args:
    print(i)

if __name__=="__main__":
   fun(1,2,3)

     