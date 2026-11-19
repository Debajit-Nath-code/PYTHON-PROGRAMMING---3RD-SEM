roll_call = {}
total_pupils = int(input("Enter number of students: "))

for _ in range(total_pupils):
    pupil = input("Enter student name: ")
    mark = input("Enter attendance (P/A): ").upper()
    roll_call[pupil] = mark

print("\nAttendance Report")
for pupil, mark in roll_call.items():
    if mark == "P":
        print(pupil, "- Present")
    else:
        print(pupil, "- Absent")
