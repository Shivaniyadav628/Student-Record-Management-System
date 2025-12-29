# Student Record Management System
# Python 3.x

import csv

# List to store students
students = []

# ---------- BASIC CRUD FUNCTIONS ----------

def add_student():
    student = {}
    student['roll_no'] = input("Enter Roll Number: ")
    student['name'] = input("Enter Name: ")
    student['class'] = input("Enter Class: ")
    student['marks'] = input("Enter Marks: ")
    students.append(student)
    print("Student added successfully!\n")


def update_student():
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student['roll_no'] == roll:
            student['name'] = input("Enter new Name: ")
            student['class'] = input("Enter new Class: ")
            student['marks'] = input("Enter new Marks: ")
            print("Student updated successfully!\n")
            return
    print("Student not found!\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student['roll_no'] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")


def search_student():
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student['roll_no'] == roll:
            print(f"Roll No: {student['roll_no']}, Name: {student['name']}, "
                  f"Class: {student['class']}, Marks: {student['marks']}\n")
            return
    print("Student not found!\n")


def display_students():
    if not students:
        print("No students to display!\n")
        return

    print("\n--- All Students ---")
    for student in students:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, "
              f"Class: {student['class']}, Marks: {student['marks']}")
    print()


# ---------- ANALYTICS FUNCTIONS ----------

def average_marks():
    if not students:
        print("No student data available.\n")
        return

    total = sum(int(student['marks']) for student in students)
    avg = total / len(students)
    print(f"Average Marks of Students: {avg:.2f}\n")


def top_student():
    if not students:
        print("No student data available.\n")
        return

    top = max(students, key=lambda s: int(s['marks']))
    print(" Top Performing Student")
    print(f"Roll No : {top['roll_no']}")
    print(f"Name    : {top['name']}")
    print(f"Class   : {top['class']}")
    print(f"Marks   : {top['marks']}\n")


def students_above_marks():
    if not students:
        print("No student data available.\n")
        return

    limit = int(input("Enter minimum marks: "))
    found = False

    print(f"\nStudents scoring above {limit}")
    for student in students:
        if int(student['marks']) >= limit:
            print(f"{student['roll_no']} | {student['name']} | {student['marks']}")
            found = True

    if not found:
        print("No students found.\n")
    else:
        print()


def sort_by_marks():
    if not students:
        print("No student data available.\n")
        return

    sorted_students = sorted(students, key=lambda s: int(s['marks']), reverse=True)
    print("\n Students Sorted by Marks (High → Low)")
    for s in sorted_students:
        print(f"{s['roll_no']} | {s['name']} | {s['marks']}")
    print()


# ---------- MAIN MENU ----------

def main():
    while True:
        print("=== Student Record Management System ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")
        print("7. Show Average Marks")
        print("8. Show Top Student")
        print("9. Students Above Given Marks")
        print("10. Sort Students by Marks")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            display_students()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        elif choice == '7':
            average_marks()
        elif choice == '8':
            top_student()
        elif choice == '9':
            students_above_marks()
        elif choice == '10':
            sort_by_marks()
        else:
            print("Invalid choice! Please enter 1-10.\n")


if __name__ == "__main__":
    main()