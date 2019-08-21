while True:
	print("Options")
	print("Enter 'add' to add")
	print("Enter 'subtract' to subtract")
	print("Enter 'multiply' to multiply")
	print("Enter 'divide to divide")
	print("Enter 'quit' to quit the program")
	user_input = input(": ")
	
	if user_input == "quit":
		break
	elif user_input == "add":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number : "))
		result = str(num1 + num2)
		print ("The answer is=" + result)
	elif user_input == "subtract":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number : "))
		result = str(num1 - num2)
		print ("The answer is=" + result)
	elif user_input == "multiply":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number : "))
		result = str(num1 * num2)
		print ("The answer is=" + result)
	elif user_input == "divide":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number : "))
		result = str(num1 / num2)
		print ("The answer is=" + result)
	elif user_input == "blarg":
		print("honk")
	else:
		print("Unknown input, please check your selection")
