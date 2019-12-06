import random
m=[[random.randint(0,10)for i in range(3)]for i in range(0,3)]
dist=map(lambda i:map(lambda j:j,i),m)
print("Printing dist")
for i in dist:
    for j in i:
        print(j)
print(m)