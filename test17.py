def funt(cls):
   print("Wrapper executed")
   def wrapper(*args):
      return cls(*args)
   return wrapper


@funt
class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(1,2)
   print(a)
   print(a.__dict__)
   

