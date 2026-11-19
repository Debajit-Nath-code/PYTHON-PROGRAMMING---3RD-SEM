with open("students.txt", "w") as out_file:
    total_records = int(input("Enter number of students: "))
    for _ in range(total_records):
        learner = input("Enter student name: ")
        id_num = input("Enter USN: ")
        out_file.write(learner + " " + id_num + "\n")

with open("students.txt", "r") as in_file:
    print("\nStudent Details:")
    print(in_file.read())
