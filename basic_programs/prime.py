
num=int(input("Enter no:"))
flag=0
for i in range(2,(num//2)+1):
    if(num%i)==0:
        flag=1
        break

    if(flag==0):
     print("no is prime")
    else:
     print("no is not prime")
    