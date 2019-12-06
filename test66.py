class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def max(self,node):
      test=node
      while test.right:
         test=test.right
      return test

   def min(self,node):
       test=node
       while test.left:
          test=test.left
       return test

   def inorder_sucessor(self,node):
       if node.right:
         return self.min(node.right)
       else:
         test=self
         prev=None
         while test:
           if test.value>node.value:
              prev=test
              test=test.left
           elif test.value<node.value:
              test=test.right
           else:
              return prev

   def search(self,node):
      test=self
      if not self:
         return None
      else:
        while test:
          if test.value>node:
             test=test.left
          elif test.value<node:
             test=test.right
          else:
             return test
        return test


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
   node.insert(18)
   node.insert(26)
   node.insert(32)
   node.insert(16)
   node.insert(5)
   node.insert(3)
   node.insert(1)
   node.insert(2)
   node.insert(7)
   test=node.search(3)
   print(node.inorder_sucessor(test).value)


