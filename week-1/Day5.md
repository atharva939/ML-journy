# Day 5 - Data Structures (Sets and Dictionaries)

## Topics Covered

* Sets
* Set operations
* Dictionaries
* Dictionary operations
* Difference between sets and dictionaries

---

## What I Learned

### 1. Sets

A set is an unordered collection of unique elements. It does not allow duplicate values.

Syntax:
my_set = {1, 2, 3}

Example:
numbers = {1, 2, 3, 3, 4}
print(numbers)

Explanation:

* Duplicate values are automatically removed
* Output will be {1, 2, 3, 4}
* Sets do not support indexing

---

### 2. Set Operations

#### Adding elements

numbers.add(5)

#### Removing elements

numbers.remove(2)

#### Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

#### Intersection

print(set1 & set2)

Explanation:

* add() inserts a new element
* remove() deletes an element
* Union combines all unique elements
* Intersection returns common elements

---

### 3. Dictionaries

A dictionary stores data in key-value pairs. It is ordered (Python 3.7+) and mutable.

Syntax:
my_dict = {"key": "value"}

Example:
student = {
"name": "Atharva",
"age": 20,
"course": "AI & DS"
}

Explanation:

* Keys must be unique
* Values can be of any data type
* Data is accessed using keys

---

### 4. Accessing Dictionary Values

Example:
print(student["name"])

Explanation:

* Returns the value associated with the given key

---

### 5. Dictionary Operations

#### Adding or updating values

student["age"] = 21

#### Adding new key

student["city"] = "Nagpur"

#### Removing a key

student.pop("course")

#### Getting keys and values

print(student.keys())
print(student.values())

Explanation:

* Dictionaries are dynamic and can be modified easily

---

### 6. Looping Through Dictionary

Example:
for key, value in student.items():
print(key, ":", value)

Explanation:

* items() returns key-value pairs
* Useful for processing structured data

---

### 7. Difference Between Set and Dictionary

| Feature    | Set                 | Dictionary              |
| ---------- | ------------------- | ----------------------- |
| Structure  | Only values         | Key-value pairs         |
| Duplicates | Not allowed         | Keys must be unique     |
| Indexing   | Not allowed         | Access using keys       |
| Use Case   | Unique data storage | Structured data storage |

---

## Code Practice

# Set example

numbers = {1, 2, 3, 3, 4}
numbers.add(5)
numbers.remove(2)
print(numbers)

# Dictionary example

student = {
"name": "Atharva",
"age": 20
}

student["city"] = "Nagpur"

for key, value in student.items():
print(key, value)

---

## My Understanding

Sets are useful for storing unique values and performing operations like union and intersection.
Dictionaries are used to store structured data and are widely used in real-world applications and machine learning.

---

## Challenges Faced

* Understanding the difference between sets and dictionaries
* Remembering dictionary methods

---

## Key Takeaways

* Sets store only unique values
* Dictionaries store data in key-value format
* Dictionaries are important for handling structured data

---

## Next Step

Learn functions and combine all concepts together
