# Program for rollercoaster ride checking height, age and "NEED PHOTO"
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
bill = 0
if height >= 120:
    print("You CAN take the rollercoaster ride!")
    if age < 12:
        bill += 5
        print("You NEED to pay $5")
    elif age <= 18:
        bill += 7
        print("You NEED to pay $7")
    elif age <= 24:
        bill += 10
        print("You NEED to pay $10")
    elif age <= 40:
        bill += 15
        print("You NEED to pay $15")
    else:
        bill += 18
        print("You NEED to pay $18")

    want_photo = input("Do you want a photo taken? Y or N: ")
    if want_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You CANNOT take the rollercoaster ride!")