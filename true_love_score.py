# Program to calculate the TRUE LOVE score
name1 = input("What is the FIRST name:\n")
name2 = input("What is the SECOND name:\n")
combined_name = name1 + name2
print(combined_name)
lower_case_name = combined_name.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
true = t + r + u + e
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
o = lower_case_name.count("o")
love = l + o + v + e
score = int(str(true) + str(love))
if score <10 or score >90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
