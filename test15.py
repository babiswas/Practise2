class Decorate:
    def __init__(self,fun):
        self.fun=fun
    def __call__(self,*args):
        return self.fun(*args)

@Decorate
def fun(*args):
   for i in args:
      print(i)

if __name__=="__main__":
   fun(1,2,3)
