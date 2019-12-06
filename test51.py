def decorate(cls):
   print("Wrapper executed")
   def wrapper(*args):
     print("Wrapper Executed")
     return cls(*args)
   return wrapper


@decorate
class A:
   def __init__(self,a,b,*args):
       self.a=a
       self.b=b
       self.l=args
   def __repr__(self):
      return f"{self.a} and {self.b}"

   def print_all(self):
      for i in self.l:
        print(i)

if __name__=="__main__":
   a=A(5,6,7,8)
   a.print_all()
   print(a)

