print("Program to find the BMI INDEX")
weight = int(input("Enter your weight in KG: "))
height = float(input("Enter your height in METERS: "))
BMI = weight / (height * height)
print("Your BMI is: ", BMI)
if BMI < 18.5:
  print (f"Your BMI is: {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is: {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is: {BMI}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is: {BMI}, you are obese.")
else:
  print(f"Yor BMI is: {BMI}, you are clinically obese.")