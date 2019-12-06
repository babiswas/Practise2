class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
   def right_view(self):
       queue=[]
       queue.append(self)
       while queue:
          q_len=len(queue)
          print(queue[-1].value)
          while q_len:
              m=queue.pop(0)
              if m.left:
                 queue.append(m.left)
              if m.right:
                 queue.append(m.right)
              q_len=q_len-1

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
   node.insert(24)
   node.insert(17)
   node.insert(20)
   node.insert(21)
   node.insert(7)
   node.insert(4)
   node.insert(5)
   node.insert(1)
   node.right_view()

