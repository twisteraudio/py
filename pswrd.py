import random

while True:

	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$^&'

	print("Options")
	print("PassGen")
	print("blarg")
	print("quit")
	user_input = input(" >>")
	
	if user_input == "quit":
		Break
	elif user_input == "blarg":
		print("honk")
	elif user_input == "PassGen":
		length = input('password length >>')
		length = int(length)
		for p in range(3):
			password = ''
			for c in range(length):
				password += random.choice(chars)
		result = password
		print("Your password is >> " + password)
	else:
		print("Unknown input, please try again")