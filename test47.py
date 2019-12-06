class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def preorder(self):
       stack=[]
       stack.append(self)
       while stack:
          m=stack.pop()
          print(m.value)
          if m.right:
             stack.append(m.right)
          if m.left:
             stack.append(m.left)
          
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
   node.insert(23)
   node.insert(25)
   node.insert(27)
   node.insert(16)
   node.insert(13)
   node.insert(5)
   node.insert(10)
   node.insert(11)
   node.insert(8)
   node.insert(2)
   node.insert(4)
   node.preorder()

