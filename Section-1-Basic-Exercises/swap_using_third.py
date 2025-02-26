a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Original values: ", a,b)

temp=a
a=b
b=temp

print("Swapped values: ",a,b)