def longest_subsequence_palindrome(str1):
    maxm=0
    table=[[0 for i in range(0,len(str1))] for i in range(0,len(str1))]
    if len(str1)>2:
      for i in range(len(str1)):
         table[i][i]=1
         maxm=1

      for i in range(0,len(str1)):
         if i+1<len(str1):
             if str1[i]==str1[i+1]:
                table[i][i+1]=2
             else:
                table[i][i+1]=1
             if table[i][i+1]>maxm:
                maxm=table[i][i+1]

      for i in range(0,len(str1)):
        for j in range(3,len(str1)+1):
           if j+i-1<len(str1):
              if str1[i]==str1[j+i-1]:
                 table[i][j+i-1]=table[i+1][j+i-2]+2
              else:
                 table[i][j+i-1]=max(table[i][j+i-2],table[i+1][j+i-1])
              if table[i][j+i-1]>maxm:
                 maxm=table[i][j+i-1]
      print(maxm)
      print(table)

if __name__=="__main__":
   longest_subsequence_palindrome("bessdedddsdddwkjjhj")
   


             