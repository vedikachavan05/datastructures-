def numofsteps(num):
    count=0
    if(num%2==0):
        while(num>0):
            num=num//2
            count+=1
    else:
        while(num>0):
            num=num-1
            count+=1
    return count

num=5
print("step required",numofsteps(num))
