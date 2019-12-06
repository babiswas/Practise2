def decorate(func):
   print("Decorator executed")
   def wrapper(*args):
      print("Executing Wrapper")
      return func(*args)
   return wrapper

@decorate
def func(*args):
   for i in args:
      print(i)

if __name__=="__main__":
  func(1,2,3,4,5)
