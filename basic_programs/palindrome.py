num=int(input("Enter no"))
sum=0
n=num
while(n>0):
    d=n%10
    sum=sum*10+d
    n=n//10

if(sum==num):
    print("the no is palindrome")
else:
    print("the no is not palindrome")

