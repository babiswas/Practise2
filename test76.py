import sys
def string_splitter(str1,chunk_size):
    l=[]
    index=0
    if len(str1)>=chunk_size:
       while (chunk_size+index)<len(str1):
            l.append(str1[index:chunk_size+index])
            index=index+chunk_size
       if str1[index:]:
          l.append(str1[index:])
       return l

if __name__=="__main__":
   m=string_splitter(sys.argv[1],int(sys.argv[2]))
   print(m)

   

      