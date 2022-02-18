# cook your dish here
t = int(input())
while t:
    n, arr = int(input()), list(map(int, input().split()))
    s = len(set(arr))
    c = n - s
    print(c)
    t-=1   
    
