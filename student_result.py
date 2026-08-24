def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def student_result(name, marks):
    average = calculate_average(marks)
    grade = calculate_grade(average)

    return {
        "name": name,
        "average": average,
        "grade": grade
    }


if __name__ == "__main__":
    result = student_result("Ankita", [85, 90, 78, 88, 92])

    print("Student Result")
    print("----------------")
    print("Name:", result["name"])
    print("Average:", result["average"])
    print("Grade:", result["grade"])