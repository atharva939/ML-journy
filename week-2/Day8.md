# Day 8 - NumPy Basics

## Topics Covered

* Introduction to NumPy
* Arrays vs Lists
* Creating NumPy arrays
* Basic operations on arrays

---

## What I Learned

### 1. Introduction to NumPy

NumPy (Numerical Python) is a library used for numerical computations in Python.
It provides support for arrays, matrices, and mathematical operations.

NumPy is faster than Python lists because it is implemented using optimized C code.

---

### 2. Arrays vs Lists

| Feature    | Python List | NumPy Array                |
| ---------- | ----------- | -------------------------- |
| Speed      | Slower      | Faster                     |
| Operations | Limited     | Supports vector operations |
| Memory     | More        | Less                       |

Example:
Python List:
a = [1, 2, 3]

NumPy Array:
import numpy as np
arr = np.array([1, 2, 3])

---

### 3. Creating NumPy Arrays

Example:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.zeros(3)
arr3 = np.ones(3)

Explanation:

* np.array() creates an array
* np.zeros() creates array of zeros
* np.ones() creates array of ones

---

### 4. Basic Array Operations

Example:
arr = np.array([1, 2, 3])

print(arr + 2)
print(arr * 2)

Explanation:

* Operations are applied to all elements
* This is called vectorization

---

### 5. Array Properties

Example:
print(arr.shape)
print(arr.size)
print(arr.dtype)

Explanation:

* shape → dimensions of array
* size → number of elements
* dtype → data type of elements

---

## Code Example

import numpy as np

arr = np.array([1, 2, 3])

print("Array:", arr)
print("Add 2:", arr + 2)
print("Multiply by 2:", arr * 2)

---

## My Understanding

NumPy arrays are more efficient than Python lists and allow fast mathematical operations.
Vectorized operations make code shorter and faster.
NumPy is the foundation for data analysis and machine learning.

---

## Challenges Faced

* Understanding difference between list and array
* Learning NumPy syntax

---

## Key Takeaways

* NumPy is faster than Python lists
* Arrays support vectorized operations
* NumPy is essential for machine learning

---

## Next Step

Learn array indexing, slicing, and advanced operations
