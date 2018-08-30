num = int(input("Given number is:"))
temp =  num
rev = 0
if(num > 0):
	rem = num % 10
	rev = rev * 10 + rem
	num = num / 10
	print("palindrome")
else:
	print("no")
	
