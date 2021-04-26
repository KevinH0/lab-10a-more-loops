string = input("Give me a number that is greater than 100.")
num = int(string)
while num<100:
	print(str(num) +" is less than 100, Try again.")
	string = input("Give me a number that is greater than 100.")
	num = int(string)
print(str(num) +" is greater than 100. Nice.")