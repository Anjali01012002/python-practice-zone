n = int(input("Enter the number: "))

rev_number=str(n)[::-1]

print(rev_number)

if n==int(rev_number):
	print("the given number is palindrome")
else:
	print("not palindrome")