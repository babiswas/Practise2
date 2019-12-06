from math import log10

def getvalue(str1,index,length):
   if index+length>len(str1):
     return -1
   value=0
   for i in range(0,length):
       c=int(str1[index+i])
       if int(c)<0 or int(c)>9:
         return -1
       value=value*10+c
   return value

def find_missing_no(str1,max_digit):
   number=0
   for i in range(1,max_digit):
      n=getvalue(str1,0,i)
      missing=-1
      j=i
      fail=False
      while j<len(str1):
         if missing==-1 and getvalue(str1,j,1+int(log10(n+2)))==n+2:
            missing=n+1
            n=n+2
            number=1+int(log10(n))
         elif getvalue(str1,j,1+int(log10(n+2)))==n+1:
            n=n+1
            number=1+int(log10(n))
         else:
           fail=True
           break
         j=j+number
      if not fail:
         return missing
   return -1

if __name__=="__main__":
   print(find_missing_no("99101102",6))
   



   



