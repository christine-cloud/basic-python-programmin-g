x=int(input())
count=0
for i in range (0,x):
  while x!=0:
    k=x%10
    count+=1
    x=x//10
print(count)

