# 10.3 Grading Rules - Tuple to store fixed grade categories
GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")


def calculate_average(scores):
    """Return the average score"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_grade(score):
    """Return the student's grade based on grading rules"""
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


def count_passed(students):
    """Return the number of passing students (grades other than 'Fail')"""
    count = 0
    for student in students:
        if student["grade"] != "Fail":
            count += 1
    return count


def main():
    students = []
    print("=== Enter Student Information (At least 5 students) ===")

    # 1. Accept data for at least five students with validation
    while len(students) < 5:
        print(f"\nStudent {len(students) + 1}:")
        name = input("Enter name: ").strip()
        
        # Age validation
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid input! Age must be an integer. Try again.")
            continue

        # Study Hours validation
        try:
            study_hours = float(input("Enter study hours: "))
        except ValueError:
            print("Invalid input! Study hours must be a number. Try again.")
            continue

        # Score validation (0 to 100)
        try:
            score = float(input("Enter Python score (0-100): "))
            if score < 0 or score > 100:
                print("Error: Score must be between 0 and 100. Please re-enter this student's data.")
                continue
        except ValueError:
            print("Invalid input! Score must be a number between 0 and 100. Try again.")
            continue

        # Classify grade
        grade = classify_grade(score)

        # Store each student using a dictionary and add to list
        student_record = {
            "name": name,
            "age": age,
            "study_hours": study_hours,
            "score": score,
            "grade": grade
        }
        students.append(student_record)

    # 2. Process all student records to compute summary statistics
    scores_list = [s["score"] for s in students]
    total_students = len(students)
    avg_score = calculate_average(scores_list)
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    passed_count = count_passed(students)
    failed_count = total_students - passed_count

    # Find the top student(s) based on the highest score
    top_students = [s["name"] for s in students if s["score"] == highest_score]
    top_student_str = ", ".join(top_students)

    # 3. Display Complete Performance Report
    print("\n===== STUDENT PERFORMANCE REPORT =====")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Study Hours: {student['study_hours']}")
        print(f"Score: {student['score']}")
        print(f"Grade: {student['grade']}\n")

    print("===== SUMMARY =====")
    print(f"Total Students: {total_students}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Passed Students: {passed_count}")
    print(f"Failed Students: {failed_count}")
    print(f"Top Student: {top_student_str}")


if __name__ == "__main__":
    main()