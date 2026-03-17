# Day 1 - Python Basics

## Topics Covered

* Variables
* Data Types
* Input and Output
* Type Casting

---

## What I Learned

### Variables

Variables are used to store data in Python.

Example:
name = "Atharvaa"
price = 20

---

### Data Types

Python supports different types of data:

* String → "Atharvaa"
* Integer → 20
* Float → 5.8
* Boolean → True

---

### Input and Output

* input() is used to take input from the user
* print() is used to display output

Example:
name = input("Enter your name: ")
print("Hello, " + name + "!")

---

### Type Casting

Type casting is used to convert one data type into another.

Example:
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

---

## Code Practice

name = "Atharvaa"
price = 20

print(price)

# Different data types

name = "Atharvaa"
age = 20
height = 5.8
is_student = True

# Input and output

name = input("Enter your name: ")
print("Hello, " + name + "!")

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Type casting

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("Your age is " + str(age) + " and your height is " + str(height) + ".")

---

## My Understanding

Python is easy to learn and beginner-friendly.
It allows dynamic typing, so we do not need to define data types explicitly.
Type casting is important when taking input from users.

---

## Challenges Faced

* Understanding how input() always takes string by default
* Needed type casting to perform calculations

---

## Next Step

Learn control flow (if, else, elif)
