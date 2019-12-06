class Node:
   def __init__(self,value):
      self.value=value
      self.next=None


class Linklist:
   def __init__(self):
      self.head=None

   def display(self):
      test=self.head
      while test:
        print(test.value)
        test=test.next

   def reverse(self):
       curr=self.head
       prev=None
       next=None
       while curr:
         next=curr.next
         curr.next=prev
         prev=curr
         curr=next
       self.head=prev
       

   def add_node_append(self,value):
       node=Node(value)
       if not self.head:
          self.head=node
       else:
          test=self.head
          while test.next:
             test=test.next
          test.next=node
       return self.head


if __name__=="__main__":
   l=Linklist()
   l.add_node_append(2)
   l.add_node_append(3)
   l.add_node_append(4)
   l.add_node_append(5)
   l.display()
   print("Reversing the list")
   l.reverse()
   l.display()



