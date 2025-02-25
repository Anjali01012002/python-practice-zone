num = int(input("Enter 4-digit integer: "))
original_num=num
rev_num = 0 

while num>0:
	digit=num%10
	rev_num = rev_num*10+digit
	num=num//10
print("Reversed number: ", rev_num)

if original_num==rev_num:
	print("The number is the same when reversed ")
else:
	print("Not same")