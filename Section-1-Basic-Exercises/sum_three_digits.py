num = int(input("Enter a three-digit integer: ")) 
sum_digits=0

while num>0:
	sum_digits=sum_digits+num%10
	num=num//10
print("Sum of three digits: ",sum_digits)