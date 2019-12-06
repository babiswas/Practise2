def longest_palindromic_substring(str1):
    maxm=0
    index1=0
    index2=0
    table=[[0 for i in range(len(str1))] for i in range(len(str1))]
    if len(str1)>=2:
       for i in range(0,len(str1)):
           table[i][i]=1
           maxm=1
       for i in range(0,len(str1)):
          if i+1<len(str1):
             if str1[i]==str1[i+1]:
                table[i][i+1]=1
                maxm=2

       for j in range(3,len(str1)):
          for i in range(0,len(str1)):
              if j+i-1<len(str1):
                 if str1[i]==str1[j+i-1]:
                     if table[i+1][j+i-2]==1:
                        table[i][j+i-1]=1
                        if j>maxm:
                          maxm=j
                          index1=i
                          index2=j+i-1
                 else:
                     table[i][j+i-1]=0
       print(maxm)
       print(str1[index1:index2+1])
       print(table)
if __name__=="__main__":
   longest_palindromic_substring("edgggskkkksswswkkswees")
   
                           
        