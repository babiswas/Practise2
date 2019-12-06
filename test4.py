class A:
   def __new__(cls,*args):
      print("New function executed")
      return object.__new__(cls)
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __repr__(self):
       return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(2,3)
   print(a)
