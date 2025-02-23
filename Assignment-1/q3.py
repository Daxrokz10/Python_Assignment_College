# WAP to create a user define function and perform separate arithmetic Operator.

def sum(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
def mod(n1,n2):
    print(n1%n2)

n1 = int(input("Enter the value for n1: "))
n2 = int(input("Enter the value for n2: "))

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for divison")
print("Enter 5 for modulo")

choice = int(input("Enter the value for choice: "))

if(choice == 1):
    sum(n1,n2)

if(choice == 2):
    sub(n1,n2)

if(choice == 3):
    mul(n1,n2)

if(choice == 4):
    div(n1,n2)

if(choice == 5):
    mod(n1,n2)
