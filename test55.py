from abc import abstractmethod,ABC

class A(ABC):
  def __init__(self,a):
     self.a=a
  def __str__(self):
     return f"{self.a}is value"
  @abstractmethod
  def get_a(self):
      pass
  

class B(A):
   def __init__(self,*args):
      A.__init__(self,*args)
   def display(self):
      print("Class B executed")

class C(A):
   def __init__(self,*args):
      A.__init__(self,*args)
   def get_a(self):
      return self.a
   

if __name__=="__main__":
   a=C(3)
   print(a)
   
   
   

   