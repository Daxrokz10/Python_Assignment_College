l=[1,2,3,4,5,5,6,7,8,9,10]
print(l)
l1=[]
l2=[]
for l in l:
    if l in l1:
        l2.append(l)
    else:
        l1.append(l)   
print('Duplicates are:')
print(l2)         