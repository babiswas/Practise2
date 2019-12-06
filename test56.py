import sys

def sample_name():
   if sys.argv[1]=="hello":
      print("hello")
   elif sys.argv[1]=="bye":
      sys.exit(2)
   print("Task Complete")

if __name__=="__main__":
   sample_name()
