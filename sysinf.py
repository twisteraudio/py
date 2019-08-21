import platform
import os

while True:

    print(platform.uname())
    user_input = input('>> ')

    if user_input == 'q':
        os.system('cls')
        break
    else:
        print('unknown input')
