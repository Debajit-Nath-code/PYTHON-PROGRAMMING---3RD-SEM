MIN_PASS = 40.0

def get_letter_grade(avg_score):
    if avg_score >= 90:
        return "A+"
    if avg_score >= 80:
        return "A"
    if avg_score >= 70:
        return "B"
    if avg_score >= 60:
        return "C"
    if avg_score >= 50:
        return "D"
    return "F"

def get_course_total():
    while True:
        try:
            num_courses = int(input("Enter number of subjects: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if num_courses > 0:
            return num_courses
        print("Number of subjects must be positive.")

def get_course_score(course_idx):
    while True:
        try:
            score = float(input(f"Enter marks for Subject {course_idx}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 0 <= score <= 100:
            return score
        print("Marks must be between 0 and 100.")

def run_app():
    print("========== STUDENT GRADING AUTOMATION ==========")
    learner_name = input("Enter Student Name: ").strip()
    reg_id = input("Enter USN: ").strip()
    num_courses = get_course_total()
    score_list = [get_course_score(idx) for idx in range(1, num_courses + 1)]

    sum_scores = sum(score_list)
    avg_score = sum_scores / num_courses
    is_passed = all(score >= MIN_PASS for score in score_list)
    outcome = "PASS" if is_passed else "FAIL"
    letter = get_letter_grade(avg_score) if is_passed else "F"

    print("\n================ GRADE REPORT =================")
    print(f"Student Name : {learner_name}")
    print(f"USN          : {reg_id}")
    print(f"Total Marks  : {sum_scores:.2f} / {num_courses * 100}")
    print(f"Average      : {avg_score:.2f}")
    print(f"Result       : {outcome}")
    print(f"Grade        : {letter}")
    print("===============================================")

if __name__ == "__main__":
    run_app()
