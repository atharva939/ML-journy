# Day 4 - Data Structures (Lists and Tuples)

## Topics Covered

* Lists
* List operations
* List methods
* Tuples
* Difference between lists and tuples

---

## What I Learned

### 1. Lists

A list is a collection of multiple items stored in a single variable. Lists are ordered, mutable (changeable), and allow duplicate values.

Syntax:
my_list = [1, 2, 3, 4]

Example:
numbers = [10, 20, 30, 40]
print(numbers)

Explanation:

* Elements are stored in order
* Indexing starts from 0
* numbers[0] gives 10

---

### 2. Accessing Elements

Elements in a list can be accessed using index values.

Example:
numbers = [10, 20, 30, 40]
print(numbers[1])   # Output: 20
print(numbers[-1])  # Output: 40

Explanation:

* Positive index starts from 0
* Negative index starts from the end

---

### 3. List Operations

#### Adding elements

numbers.append(50)

#### Inserting elements

numbers.insert(1, 15)

#### Removing elements

numbers.remove(20)

#### Popping elements

numbers.pop()

Explanation:

* append() adds element at the end
* insert() adds at a specific index
* remove() deletes a specific value
* pop() removes last element

---

### 4. List Slicing

Slicing is used to access a range of elements.

Example:
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Output: [20, 30, 40]

Explanation:

* Start index is included
* End index is excluded

---

### 5. Looping Through Lists

Example:
numbers = [10, 20, 30]

for num in numbers:
print(num)

Explanation:

* Loop iterates through each element
* Useful for processing data

---

### 6. Tuples

A tuple is similar to a list but immutable (cannot be changed after creation).

Syntax:
my_tuple = (1, 2, 3)

Example:
data = (10, 20, 30)
print(data[0])

Explanation:

* Elements cannot be modified
* Faster than lists
* Used for fixed data

---

### 7. Difference Between List and Tuple

| Feature     | List         | Tuple      |
| ----------- | ------------ | ---------- |
| Mutability  | Mutable      | Immutable  |
| Syntax      | []           | ()         |
| Performance | Slower       | Faster     |
| Use Case    | Dynamic data | Fixed data |

---

## Code Practice

# List example

numbers = [10, 20, 30, 40]

numbers.append(50)
numbers.insert(1, 15)
numbers.remove(30)

print(numbers)

# Loop through list

for num in numbers:
print(num)

# Tuple example

data = (1, 2, 3)
print(data[1])

---

## My Understanding

Lists are very useful for storing and modifying data dynamically.
Tuples are useful when data should not be changed.
Lists will be heavily used in machine learning for handling datasets.

---

## Challenges Faced

* Remembering different list methods
* Understanding slicing properly

---

## Key Takeaways

* Lists are mutable and flexible
* Tuples are immutable and faster
* Looping through lists is important for data processing

---

## Next Step

Learn sets and dictionaries and understand how they store data efficiently
