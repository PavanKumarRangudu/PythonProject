#  Calculating the average height of a class
number_of_students = int(input("Enter the number of students in the class:\n"))

list_of_heights = []
for num in range(0, number_of_students):
    height = int(input(f"Enter the height of the student{num + 1}:\n"))
    list_of_heights.append(height)

sum_of_heights = 0
for height in list_of_heights:
    sum_of_heights += height

number_of_students = 0
for num in list_of_heights:
    number_of_students += 1

average_height = round(sum_of_heights / number_of_students)

print(f"total height = {sum_of_heights}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")