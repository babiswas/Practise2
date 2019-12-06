class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def insert(self,data):
       if self.value>data:
          if self.left:
             self.left.insert(data)
          else:
             self.left=Node(data)
       elif self.value<data:
          if self.right:
             self.right.insert(data)
          else:
             self.right=Node(data)
       else:
          print("Duplication not allowed")

   def inorder(self):
      stack=[]
      test=self
      while True:
          if test:
             stack.append(test)
             test=test.left
          elif stack:
             test=stack.pop()
             print(test.value)
             test=test.right
          else:
             break

if __name__=="__main__":
   node=Node(12)
   node.insert(23)
   node.insert(25)
   node.insert(20)
   node.insert(16)
   node.insert(18)
   node.insert(5)
   node.insert(7)
   node.insert(1)
   node.insert(3)
   node.inorder()

             
         
         