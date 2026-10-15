N=int(input("enter the no of elements in array:"))
l1=[]
for i in range(0,N):
  n=int(input("enter no:"))
  l1.append(n)
move=0
l2=[]
l3=[]
for i in l1:
  if(i==move):
    l2.append(i)
  else:
    l3.append(i)

final_list=l2+l3



'''
l3=[]
for j in range(N-1,-1,-1):
  l3.append(l2[j])

print("list ending with zero")
print(l3)
'''
print(final_list)
