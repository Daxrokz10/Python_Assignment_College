t=(1,2,3,4,5,6,7)
t1=(7,6,5,4,3,2,1)
print(t)
print(t1)
t2=sorted(t1)
t3=sorted(t1)
if t2==t3:
    print('Both tuples are Anagram')
else:
    print('Both tuples are not Anagram')    