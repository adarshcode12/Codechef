# to remove duplicate in list convert into set 
# list can be converted to set and set to list
a={1,2,3,4,5} 
print(a)
b=list(a)
print(b)
b.append(3)
print(b)
c=set(b)
print(c)
# remove duplicate without using the list or set
# initializing list 
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i)