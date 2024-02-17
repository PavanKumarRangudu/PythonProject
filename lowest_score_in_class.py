# Program to print the lowest score in the class
number_of_students = int(input("Enter the number of students in the class:\n"))

list_of_scores = []
for num in range(0, number_of_students):
    score = int(input(f"Enter the score of student{num + 1}:\n"))
    list_of_scores.append(score)
print(list_of_scores)

lowest_score = list_of_scores[0]
for score in list_of_scores:
    if score < lowest_score:
        lowest_score = score

print(f"The lowest score in the class is: {lowest_score}")
print(min(list_of_scores))