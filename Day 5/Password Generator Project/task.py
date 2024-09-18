from random import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
'''easy_version
password = ""
random_letters = ""
random_symbols = ""
random_number = ""
for i in range(nr_letters):
    random_letter = random.choice(letters)
    password += random_letter
for j in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
for k in range(nr_numbers):
    random_number = random.choice(numbers)
    password += random_number
print(f"Your password is: {password}")'''

'''
import random
l = list(s)
random.shuffle(l)
result = ''.join(l)
'''

#Hard version
password_list = []
random_letters = ""
random_symbols = ""
random_number = ""
for i in range(nr_letters):
    random_letter = random.choice(letters)
    password_list += random_letter
for j in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password_list += random_symbol
for k in range(nr_numbers):
    random_number = random.choice(numbers)
    password_list += random_number

random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")