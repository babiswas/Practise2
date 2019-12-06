def decorate(func):
  print("Wrapper executed")
  def wrapper(*args):
      return func(*args)
  return wrapper

@decorate
def fun(*args):
  for i in args:
    print(i)

if __name__=="__main__":
   fun(1,2,3)
