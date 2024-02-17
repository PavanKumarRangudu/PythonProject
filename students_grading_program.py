# Students Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# METHOD 1
# for name in student_scores:
#     score = student_scores[name]
#     # print(score)
#     if score > 90:
#         student_scores[name] = "Outstanding"
#     elif 90 > score > 80:
#         student_scores[name] = "Exceeds Expectations"
#     elif 80 > score > 70:
#         student_scores[name] = "Acceptable"
#     else:
#         student_scores[name] = "Fail"
# print(student_scores)
# METHOD 2
student_grades = {}
for name in student_scores:
    # print(student_scores[name])
    if student_scores[name] > 90:
        student_grades[name] = "Outstanding"
    elif 90 > student_scores[name] > 80:
        student_grades[name] = "Exceeds Expectations"
    elif 80 > student_scores[name] > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"
print(student_grades)
# METHOD 3
# student_grades = {}
# student_grades["Harry"] = "Exceeds Expectations"
# student_grades["Ron"] = "Acceptable"
# student_grades["Hermione"] = "Outstanding"
# student_grades["Draco"] = "Acceptable"
# student_grades["Neville"] = "Fail"
