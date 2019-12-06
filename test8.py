def palindrome(str1):
   str2=str1[::-1]
   if str2==str1:
       return True
   return False

def sub_str(str1):
   substr=[]
   if len(str1)>1:
      for i in range(0,len(str1)):
          for j in range(1,len(str1)+1):
              if i+j-1<len(str1):
                 substr.append(str1[i:j+i])
   for i in substr:
      print(i)
   return substr

if __name__=="__main__":
   m=sub_str("abbsebbsannddassa")
   max=0
   for i in m:
      if palindrome(i):
         print(i)
         length=len(i)
         if length>max:
            max=length
   print(max)

       
   