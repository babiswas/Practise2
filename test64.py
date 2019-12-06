class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def reverse_level_order(self):
       queue=[]
       stack=[]
       queue.append(self)
       while queue:
          m=queue.pop(0)
          stack.append(m)
          if m.right:
            queue.append(m.right)
          if m.left:
            queue.append(m.left)
       while stack:
          print(stack.pop().value)
          
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
   node.insert(21)
   node.insert(17)
   node.insert(15)
   node.insert(14)
   node.insert(5)
   node.insert(7)
   node.insert(6)
   node.insert(4)
   node.insert(1)
   node.insert(2)
   node.reverse_level_order()


        