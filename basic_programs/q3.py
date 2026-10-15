N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)

count1=0
count2=0

for i in range (0,N):
  if(l1[i]%2==0):
    count1+=1
  else:
    count2+=1

print("even no count",count1)
print("odd no count",count2)

