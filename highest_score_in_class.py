# Program to print the highest score in the class
number_of_students = int(input("Enter the number of students in the class:\n"))

list_of_scores = []
for num in range(0, number_of_students):
  score = int(input(f"Enter the score of student{num + 1}:\n"))
  list_of_scores.append(score)
print(list_of_scores)

highest_score = 0
for score in list_of_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")
print(max(list_of_scores))