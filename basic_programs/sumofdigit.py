num=int(input("Enter no"))
sum=0
while(num>0):
    d=num%10
    sum+=d
    num=num//10
print(sum)

