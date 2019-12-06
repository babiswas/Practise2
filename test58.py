class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
       self.level=0
   def vertical_trav(self):
       queue=[]
       key_val={}
       queue.append(self)
       while queue:
         m=queue.pop(0)
         if m.level not in key_val:
            key_val[m.level]=[]
            key_val[m.level].append(m.value)
         else:
            key_val[m.level].append(m.value)
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

if __name__=="__main__":
   node=Node(12)
   node.insert(23)
   node.insert(25)
   node.insert(21)
   node.insert(18)
   node.insert(19)
   node.insert(5)
   node.insert(1)
   node.insert(10)
   node.insert(2)
   node.vertical_trav()

