l=[1,2,3,4,5,6,7,8,9,10]
print(l)
n=l[2]
l[2]=l[3]
l[3]=n
t=tuple(l)
print(t)