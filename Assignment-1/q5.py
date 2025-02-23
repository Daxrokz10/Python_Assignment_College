# WAP to declare local variable

a=10
print(a)

def func():
    print("Just a func")
    a=11
    print(a)

func()

print(a,"It remains unchanged because global wasn't accessed")

