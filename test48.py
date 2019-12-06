class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
      stack1=[]
      stack2=[]
      stack1.append(self)
      while stack1:
         m=stack1.pop()
         stack2.append(m)
         if m.left:
            stack1.append(m.left)
         if m.right:
            stack1.append(m.right)
      while stack2:
         print(stack2.pop().value)
         
      
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
          print("Duplicacy not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(24)
   node.insert(23)
   node.insert(27)
   node.insert(21)
   node.insert(18)
   node.insert(5)
   node.insert(7)
   node.insert(4)
   node.insert(2)
   node.insert(1)
   node.postorder()


       
