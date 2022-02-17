aa=int(input())
count=0
for i in range(1,aa):
    if(i%2==0 and (aa-i)%2==0):
        count+=1
        break
    else:
        count=0
if count==1:
    print("YES")
else:
    print('NO')