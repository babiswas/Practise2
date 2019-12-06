class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
       self.level=0
   def vertical_trav(self):
       queue=[]
       key_val=dict()
       queue.append(self)
       while queue:
         m=queue.pop()
         if m.level not in key_val:
            key_level[m.level]=[]
         key_level[m.level].append(m.value)
         if m.left:
            queue.append(m.left)
         if m.right:
            queue.append(m.right)
       for i in sorted(key_val.keys()):
          for j in key_val[i]:
             print(j)
          
          
   def insert(self,data):
      if self.value>data:
         if self.left:
            self.left.insert(data)
         else:
            self.left=Node(data)
            self.left.level=self.level-1
      elif self.value<data:
         if self.right:
            self.right.insert(data)
         else:
            self.right=Node(data)
            self.right.level=self.level+1
      else:
         print("Duplicacy not allowed")
