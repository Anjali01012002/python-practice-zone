num = int(input("Enter an integer: "))
while num>0:
	digit=num%10
	print(digit, end=" ")
	num=num//10