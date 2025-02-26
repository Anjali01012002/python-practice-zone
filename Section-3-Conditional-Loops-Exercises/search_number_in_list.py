l1 = [4,5,6,2,3,9,1,4,5,6,3]

num = int(input("Enter the number: "))

for i in l1:
	if i==num:
		print("Number exist.")
		break
else:
	print("Number not exist.")
