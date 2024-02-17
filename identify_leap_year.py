# Program to IDENTIFY if an YEAR is a LEAP YEAR or NOT
year = int(input("Enter a year: "))
if (year % 4) != 0:
  print("Not leap year")
elif (year % 100) != 0:
   print ("Leap year")
elif (year % 400) != 0:
  print("Not leap year")
else:
  print("Leap year")