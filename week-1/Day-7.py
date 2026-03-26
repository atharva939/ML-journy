# Day 7 - Mini Project
# Student Management System

students = []

# -------------------------------
# Function to add student
# -------------------------------
def add_student(name, marks):
    student = {
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully")

# -------------------------------
# Function to display students
# -------------------------------
def display_students():
    if len(students) == 0:
        print("No student records found")
    else:
        print("\nStudent Records:")
        for student in students:
            print("Name:", student["name"], "| Marks:", student["marks"])

# -------------------------------
# Function to calculate average
# -------------------------------
def calculate_average():
    if len(students) == 0:
        print("No data to calculate average")
        return

    total = 0
    for student in students:
        total += student["marks"]

    average = total / len(students)
    print("Average Marks:", average)

# -------------------------------
# Menu-driven program
# -------------------------------
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average Marks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)

    elif choice == "2":
        display_students()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice, try again")
