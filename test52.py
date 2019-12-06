class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def lvl_trav(self):
      queue=[]
      queue.append(self)
      while queue:
         m=queue.pop(0)
         print(m.value)
         if m.left:
           queue.append(m.left)
         if m.right:
           queue.append(m.right)

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
   node.insert(24)
   node.insert(25)
   node.insert(17)
   node.insert(19)
   node.insert(5)
   node.insert(9)
   node.insert(3)
   node.lvl_trav()

