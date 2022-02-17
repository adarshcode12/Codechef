for i in range(int(input())):
    diff1=diff2=0
    n=int(input())
    rem=n%3
    diff1= n//3
    diff2=(2*n)//3 
    if rem==1:
        diff1+=1
    if rem==2:
        diff2+=1
    print(diff1,diff2//2)