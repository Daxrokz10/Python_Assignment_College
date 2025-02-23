# WAP to declare global variable

a=10
print(a)

def func():
    print("Just a func")
    global a
    a=15
    print(a)

func()

print(a,"It gets changed because we access the global")

