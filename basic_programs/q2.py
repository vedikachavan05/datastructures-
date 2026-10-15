N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)
max=l1[1]
min=l1[1]

for i in range (1,N):
  if(l1[i]<=min):
    min=l1[i]
  elif(l1[i]>=max):
    max=l1[i]

print("minimum in list:",min)
print("maximum in list1:",max)