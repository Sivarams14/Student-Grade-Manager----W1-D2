# grade_manager.py

# A list is used so that students can have the same name.
students = []


def get_grade(mark):
    """
    Return the grade based on the student's mark.
    """

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    """
    Ask the user for a student's name and mark.
    Validate the input before storing the student.
    """

    print("\n--- Add Student ---")

    # Keep asking until a valid name is entered
    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty. Please try again.")
        else:
            break

    # Keep asking until a valid mark is entered
    while True:
        mark_input = input("Enter student mark (0-100): ").strip()

        try:
            mark = int(mark_input)

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

    grade = get_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"{name} added successfully with grade {grade}.")


def show_results():
    """
    Display all students in a neatly formatted table.
    Also display average, highest and lowest marks.
    """

    print("\n--- Student Results ---")

    # Handle the case where no students have been added
    if len(students) == 0:
        print("No students have been added yet.")
        return

    # Table heading
    print("-" * 38)
    print(f"{'Name':<20}{'Mark':>8}{'Grade':>10}")
    print("-" * 38)

    # Display each student
    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:>8}"
            f"{student['grade']:>10}"
        )

    print("-" * 38)

    # Get all marks
    marks = [student["mark"] for student in students]

    # Calculate statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Average : {average:.1f}")
    print(f"Highest : {highest}")
    print(f"Lowest  : {lowest}")


def main():
    """
    Main menu of the Student Grade Manager.
    """

    while True:

        print("\n==============================")
        print("   STUDENT GRADE MANAGER")
        print("==============================")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")
        print("==============================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("\nThank you for using Student Grade Manager.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


# Start the program
if __name__ == "__main__":
    main()