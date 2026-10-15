N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)
sum=0
for i in l1:
    sum+=i
print("Sum of array is:",sum)

