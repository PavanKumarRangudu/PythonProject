# Program for Python Pizza Deliveries
size = input("Enter the size of the Pizza required: S, M, L: \n")
add_pepperoni = input("Want pepperoni or NOT: Y or N: \n")
extra_cheese = input("Wnat extra cheese or NOT: Y or N: \n")
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size == "M":
    bill += 3
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")