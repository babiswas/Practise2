def longest_palindromic_substring(str1):
    maxm=0
    table=[[0 for i in range(len(str1))] for i in range(len(str1))]
    if len(str1)>2:
       for i in range(0,len(str1)):
           table[i][i]=1
           maxm=0
       for i in range(0,len(str1)):
          if i+1<len(str1) and str1[i]==str1[i+1]:
             table[i][i+1]=1
             maxm=2
       for i in range(3,len(str1)):
         for j in range(0,len(str1)):
            if j+i-1<len(str1) and str1[j]==str1[j+i-1]:
               if table[j+1][j+i-2]:
                  table[j][j+i-1]=1
                  if i>maxm:
                       maxm=i
       print(maxm)
       print(table)
if __name__=="__main__":
       longest_palindromic_substring("abbcdddwwwweeeasxse")
   
          