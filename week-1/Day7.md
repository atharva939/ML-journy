# Day 7 - Revision and Mini Project

## Topics Covered

* Revision of Python basics
* Applying concepts in a mini project
* Problem solving

---

## What I Did

### 1. Revision of Concepts

Revised all topics learned during the week:

* Variables and Data Types
* Input and Output
* Conditional Statements (if-else)
* Loops (for, while)
* Lists and Tuples
* Sets and Dictionaries
* Functions

---

### 2. Mini Project: Student Management System

Created a simple program to manage student data using Python concepts.

---

## Project Description

The program allows:

* Adding student details
* Displaying student records
* Calculating average marks

Concepts used:

* Lists
* Dictionaries
* Loops
* Functions

---

## Sample Code

students = []

def add_student(name, marks):
student = {
"name": name,
"marks": marks
}
students.append(student)

def display_students():
for student in students:
print(student["name"], "-", student["marks"])

def calculate_average():
total = 0
for student in students:
total += student["marks"]
return total / len(students)

# Adding sample data

add_student("Atharva", 85)
add_student("Rahul", 78)

display_students()
print("Average Marks:", calculate_average())

---

## My Understanding

This project helped me combine multiple Python concepts into a single program.
I understood how lists and dictionaries can be used to store structured data.
Functions made the code organized and reusable.

---

## Challenges Faced

* Managing data inside lists and dictionaries
* Writing logic for average calculation

---

## Key Takeaways

* Combining concepts is more important than learning individually
* Functions improve code structure
* Lists and dictionaries are useful for real-world data

---

## Next Step

Start learning NumPy and Pandas for data handling
