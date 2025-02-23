# Find datatype of variable

def find_type(variable):
    return type(variable)

var1 = 10
var2 = 10.5
var3 = "Hello"
var4 = [1, 2, 3]

print("Type of var1:", find_type(var1))
print("Type of var2:", find_type(var2))
print("Type of var3:", find_type(var3))
print("Type of var4:", find_type(var4))