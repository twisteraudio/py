#welcome to my portfolio in python
#all the little things ive scripted will be included in here

import random
import time
import datetime
import os

while True:
	
	print("    **     **   ******   **   **   **   **")
	print("   ***   ***   **       ***  **   **   **")
	print("  ** *** **   ******   ** * **   **   **")
	print(" **  *  **   **       **  ***   **   **")
	print("**     **   ******   **   **   *******")
	print("")
	print("[1] calculator")
	print("[2] password generator")
	print("[3] is it xmas")
	print("[4] tasks")
	print("[5] games")
	print("- to exit type 'quit' -")
	
	user_input = input(">> ")
	
	if user_input == "quit":
		break
	
	elif user_input == "blarg":
		os.system('cls')
		print('honk')
	
	elif user_input == "1":
		os.system('cls')
	
		while True:
			
			print("Options")
			print("Enter 'add' to add")
			print("Enter 'subtract' to subtract")
			print("Enter 'multiply' to multiply")
			print("Enter 'divide' to divide")
			print("Enter 'quit' to quit the program")
			
			user_input = input(">> ")
	
			if user_input == "quit":
				os.system('cls')
				break
			
			elif user_input == "add":
				os.system('cls')
				num1 = float(input("Enter a number: "))
				num2 = float(input("Enter another number : "))
				result = str(num1 + num2)
				print ("The answer is=" + result)
			
			elif user_input == "subtract":
				os.system('cls')
				num1 = float(input("Enter a number: "))
				num2 = float(input("Enter another number : "))
				result = str(num1 - num2)
				print ("The answer is=" + result)
			
			elif user_input == "multiply":
				os.system('cls')
				num1 = float(input("Enter a number: "))
				num2 = float(input("Enter another number : "))
				result = str(num1 * num2)
				print ("The answer is=" + result)
			
			elif user_input == "divide":
				os.system('cls')
				num1 = float(input("Enter a number: "))
				num2 = float(input("Enter another number : "))
				result = str(num1 / num2)
				print ("The answer is=" + result)
			
			elif user_input == "blarg":
				os.system('cls')
				print("honk")
			
			else:
				os.system('cls')
				print("Unknown input, please check your selection")
			
	elif user_input == "2":

		os.system('cls')
		
		while True:
			chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$^&'

			print("[1] Options")
			print("[2] PassGen")
			print("blarg")
			print("quit")
			
			user_input = input(">> ")
	
			if user_input == "quit":
				os.system('cls')	
				break
			
			elif user_input == "blarg":
				os.system('cls')
				print("honk")
			
			elif user_input == "1": 
				os.system('cls')
				print('this program generates a random password with the amount of digits you specify')

			elif user_input == "2":
				os.system('cls')
				length = input('password length >> ')
				length = int(length)
				
				for p in range(3):
					password = ''
					for c in range(length):
						password += random.choice(chars)
				result = password
				os.system('cls')
				print("Your password is >> " + password)
			
			else:
				os.system('cls')
				print("Unknown input, please try again")
	
	elif user_input == "3":

		os.system('cls')

		while True:
			daytoday = datetime.datetime.now().timetuple().tm_yday
			today = datetime.datetime.today()
			#christmas number = 359

			print("what is the date today? please enter in year, month, day")
			print("To exit program, type quit")
			
			user_input = input(" >>")
	
			if user_input == "quit":
				os.system('cls')
				break		
			
			elif user_input == "date today":
				os.system('cls')
				print(today)
			
			elif user_input == "check for xmas":
				os.system('cls')
				
				if int(daytoday) == 359:
					print("YES, REJOICE")
				
				elif int(daytoday) < 359:
					print("NO")
				
				elif int(daytoday) > 359:
					print("NO")
			
			else:
				os.system('cls')
				print("this was supposed ot be a fun thing, now why did you have to put that there")
	
	elif user_input == "4":
		os.system('cls')
		while(True):

			print('PLEASE SELECT THE TASK YOU WISH TO RUN')
			print('[1] top')
			print('[2] ping check')
			print('[3] get drives')
			print('[4] quit')

			unput = input('>> ')

			if unput == '4':
				os.system('cls')
				break
			
			elif unput == 'test':
				os.system('cls')
				os.system('ping 192.168.86.1 -n 3')

			elif unput == '1':
				#top
				os.system('cls')
				os.system('powershell -command "get-process | sort -desc cpu | select -f 10"')

			elif unput == '2':
				#ping check
				os.system('cls')
				while True:
					print('what is your ip?')
					user_input = input('>> ')
					
					if user_input == 'quit':
						os.system('cls')
						break
					
					else:
						ipcheck = user_input
						response = os.system('ping -n 5' + ipcheck)
						
						if response <= 0:
							print(ipcheck, 'is down')
						
						else:
							print(ipcheck, 'is up')

			elif unput == '3':
				#get drives
				os.system('cls')
				os.system('powershell -command "get-psdrive | ?{$_.free -gt 10gb}"')
			
			else:
				os.system('cls')
				print('Unknown value entered, please try again')

	elif user_input == "5":
		os.system('cls')
		print("This tab is still being worked on, please come back soon")
	
	else:
		os.system('cls')
		print('unknown input')
