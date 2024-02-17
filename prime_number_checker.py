# Program to identify if a number is a prime number or NOT
n = int(input("Enter a number: "))
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
prime_checker(number=n)
# for i in range(2, n):
#   print(i)