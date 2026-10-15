N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)
print(l1)

l2=[]

for j in range(N-1,-1,-1):
  l2.append(l1[j])

print(l2)


  
