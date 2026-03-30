# Day 9 - NumPy Advanced

## Topics Covered

* Array indexing
* Array slicing
* 2D arrays
* Reshaping arrays
* Mathematical operations
* Axis concept

---

## What I Learned

### 1. Array Indexing

Elements in a NumPy array can be accessed using index positions.

Example:
arr = np.array([10, 20, 30])
print(arr[0])

---

### 2. Array Slicing

Used to access a range of elements.

Example:
arr = np.array([10, 20, 30, 40])
print(arr[1:3])

---

### 3. 2D Arrays

NumPy supports multi-dimensional arrays.

Example:
arr = np.array([[1, 2], [3, 4]])
print(arr[0, 1])

---

### 4. Reshaping Arrays

reshape() changes the shape of an array.

Example:
arr = np.array([1, 2, 3, 4])
print(arr.reshape(2, 2))

---

### 5. Mathematical Operations

NumPy provides built-in functions.

Example:
np.sum(arr)
np.mean(arr)
np.max(arr)

---

### 6. Axis Concept

Used to perform operations across rows or columns.

Example:
np.sum(arr, axis=0)

---

## Code Example

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.reshape(2, 2))

---

## My Understanding

NumPy allows efficient manipulation of data using arrays.
Reshaping and indexing are very important for working with datasets.

---

## Challenges Faced

* Understanding axis parameter
* Working with 2D arrays

---

## Key Takeaways

* NumPy supports multi-dimensional arrays
* reshape() is important for data transformation
* axis helps in row-wise and column-wise operations

---

## Next Step

Start learning Pandas for data handling
