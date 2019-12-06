class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def spiral_trav(self):
       stack1=[]
       stack2=[]
       stack1.append(self)
       while stack1 or stack2:
           while stack1:
              m=stack1.pop()
              print(m.value)
              if m.left:
                 stack2.append(m.left)
              if m.right:
                 stack2.append(m.right)
           while stack2:
              m=stack2.pop()
              print(m.value)
              if m.right:
                 stack1.append(m.right)
              if m.left:
                 stack1.append(m.left)
          
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

if __name__=="__main__":
   node=Node(12)
   node.insert(23)
   node.insert(25)
   node.insert(27)
   node.insert(19)
   node.insert(16)
   node.insert(20)
   node.insert(5)
   node.insert(7)
   node.insert(10)
   node.insert(11)
   node.insert(4)
   node.spiral_trav()

