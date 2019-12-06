class A:
  def __init__(self,a):
     self.a=a

  def __repr__(self):
     return f"{self.a} is the value"

  def __add__(self,other):
      if isinstance(other,A):
         self.a=self.a+other.a
      elif isinstance(other,int):
         self.a=other+self.a

  def __radd__(self,other):
      if other==0:
         return self
      else:
         return self.__add__(other)

if __name__=="__main__":
   a=A(12)
   12+a
   print(a)

         