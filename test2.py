class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __repr__(self):
     return f"{self.a} and {self.b}"

  def __add__(self,other):
     if isinstance(other,A):
        self.a=self.a+other.a
        self.b=self.b+other.b
     elif isinstance(other,int):
        self.a=self.a+other
        self.b=self.b+other

  def __radd__(self,other):
      if isinstance(other,int):
         return self.__add__(other)

  @property
  def set_a(self):
    return self.a
  @property
  def set_b(self):
    return self.b
  @set_a.setter
  def set_a(self,a):
     self.a=a
  @set_b.setter
  def set_b(self,b):
     self.b=b

if __name__=="__main__":
   a=A(12,13)
   print(a)
   print(a.set_a)
   print(a.set_b)
   a.set_a=100
   a.set_b=32
   print(a)
   b=A(15,20)
   a=A(17,40)
   a+b
   print(a)
   a=A(21,20)
   10+a
   print(a)
   print(a.__dict__)
   setattr(a,'l',65)
   print(a.__dict__)

   
   

     
  