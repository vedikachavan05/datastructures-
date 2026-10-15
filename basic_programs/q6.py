N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)

l2=[]
for i in l1:
 if i not in l2:
  l2.append(i)

print(l1)
print(l2)

