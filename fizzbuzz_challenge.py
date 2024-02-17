# FizzBuzz Challenge. MOST ASKED IN INTERVIEWS.
# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” and for multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz.
number = int(input("Enter a number:\n"))
for number in range(1, number+1, 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)