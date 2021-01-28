#Password Generator Project
import random
import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letter_select = ""
number_select = ""
symbol_select = ""

pass_select = []
for letter in range(0,nr_letters-(nr_numbers+nr_symbols)):
  letter_select = random.choice(letters)
  pass_select.append(letter_select)

for number in range(0,nr_numbers):
  number_select = random.choice(numbers)
  pass_select.append(number_select)

for symbol in range(0,nr_symbols):
  symbol_select = random.choice(symbols)
  pass_select.append(symbol_select)

password_new = "" 
for password in pass_select:
  password_new += password
password_new1 = ''.join(random.sample(password_new,len(password_new)))
   
print(f"Your password is {password_new1}")