number = int(input("Enter a number"))

list = [] 

loop = 1

while loop < number :
	if number % loop == 0 :
		list.append(loop)
		
	loop = loop + 1
		
print(list)