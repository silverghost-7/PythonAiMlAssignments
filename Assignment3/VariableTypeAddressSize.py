from sys import getsizeof

print("Enter number:")
num1 = int(input())
print("Data type:",type(num1))
print("Memory Address:",id(num1))
print("Size:",getsizeof(num1))