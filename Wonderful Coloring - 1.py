for i in range(int(input())):
    red=count=0
    a=str(input())
    lenst=len(a)
    x={}
    for i in a:
        if i in x:
            x[i]+=1
        else:
            x[i]=1
    red=len(x)
    for k,j in x.items():
        if j > 2:
            count+=j
    ff=lenst-count
    red=ff//2
    print(red)