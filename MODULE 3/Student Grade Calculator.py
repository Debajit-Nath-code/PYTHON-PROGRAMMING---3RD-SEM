pupil_name = input("Enter student name: ")
score_val = float(input("Enter marks: "))

if score_val >= 90:
    letter_grade = "A"
elif score_val >= 75:
    letter_grade = "B"
elif score_val >= 60:
    letter_grade = "C"
elif score_val >= 40:
    letter_grade = "D"
else:
    letter_grade = "Fail"

print("Student Name:", pupil_name)
print("Grade:", letter_grade)
