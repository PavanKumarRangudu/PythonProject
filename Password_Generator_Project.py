#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# l = []
# s = []
# n = []
# for i in range(0, nr_letters):
#   l += letters[i]
# print("".join(l))
# for i in range(0, nr_symbols):
#   s += symbols[i]
# print("".join(s))
# for i in range(0, nr_numbers):
#   n += numbers[i]
# print("".join(n))
# print("".join(l)+"".join(s)+"".join(n))
# print("Here is your password:" + "".join(l) + "".join(s) + "".join(n))
# print("Here is your password (NOT RANDOMISED):" + "".join(letters[i] for i in range(0, nr_letters)) + "".join(symbols[i] for i in range(0, nr_symbols)) + "".join(numbers[i] for i in range(0, nr_numbers)))
password = ""
for i in range(0, nr_letters):
  password += random.choice(letters)
for i in range(0, nr_symbols):
  password += random.choice(symbols)
for i in range(0, nr_numbers):
  password += random.choice(numbers)
print("Here is your password (NOT RANDOMISED):\t" + password)
# print(type(password))
# print(len(password))
# print(len(numbers))
# password_len = nr_letters + nr_symbols + nr_numbers + 1
# random.shuffle(password)
# print(type(password))
# print(password)
# print("".join(password))
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters = random.sample(letters, nr_letters)
symbols = random.sample(symbols, nr_symbols)
numbers = random.sample(numbers, nr_numbers)
# print("Here is your password:" + "".join(letters) + "".join(symbols) + "".join(numbers))
# print("Here is your password:" + "".join(random.sample(letters, nr_letters)) + "" .join(random.sample(symbols, nr_symbols)) + "" .join(random.sample(numbers, nr_numbers)))
# print("".join(letters))
# print("".join(symbols))
# print("".join(numbers))
# print("".join(letters) + "".join(symbols) + "".join(numbers))
password = letters + symbols + numbers
# password_length = nr_letters + nr_symbols + nr_numbers
# password = random.sample(password_letters, password_length)
random.shuffle(password)
print("Here is your password (RANDOMISED):\t" + "".join(password))