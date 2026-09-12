name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

print("\nEnter marks for 3 subjects (Max 50 marks per subject):")
sub1 = float(input("Subject 1 Marks: "))
sub2 = float(input("Subject 2 Marks: "))
sub3 = float(input("Subject 3 Marks: "))

total_marks = sub1 + sub2 + sub3

average_marks = total_marks / 3

print("\nStudent Details and Marks Report")
print(f"Name: ", name)
print(f"USN: ", usn)
print(f"Branch: ", branch)
print(f"Semester: ", semester)
print(f"Subject 1: ", sub1 / 50)
print(f"Subject 2: ", sub2 / 50)
print(f"Subject 3: ", sub3 / 50)
print(f"Total: ", total_marks / 150)
print(f"Average: ", average_marks / 50)