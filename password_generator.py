import secrets
import string

print('Welcome to Password generator by D-prajwal!')

length = int(input('\nEnter the length of password: '))                      

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

password = ''.join(secrets.choice(all) for i in range(length))  

print(password)

input("Press enter to exit...")