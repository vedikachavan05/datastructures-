N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)

key=int(input("enter element to search"))

for i in range(0,N):
  if(key==l1[i]):
    index=i
    break
 
    

if(index==-1):
  print("element not found in list")
else:
  print(key,"found at position",index)
  
