# Day 4 - Lists and Tuples Practice

# -------------------------------
# 1. Creating a List
# -------------------------------
numbers = [10, 20, 30, 40]
print("Original List:", numbers)

# -------------------------------
# 2. Accessing Elements
# -------------------------------
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# -------------------------------
# 3. Adding Elements
# -------------------------------
numbers.append(50)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

# -------------------------------
# 4. Removing Elements
# -------------------------------
numbers.remove(30)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

# -------------------------------
# 5. List Slicing
# -------------------------------
numbers = [10, 20, 30, 40, 50]
print("Sliced list (1:4):", numbers[1:4])

# -------------------------------
# 6. Looping Through List
# -------------------------------
print("Looping through list:")
for num in numbers:
    print(num)

# -------------------------------
# 7. Tuple Example
# -------------------------------
data = (1, 2, 3)
print("Tuple:", data)
print("First element in tuple:", data[0])

# -------------------------------
# 8. Difference Demo
# -------------------------------
# Lists can be modified
numbers[0] = 100
print("Modified list:", numbers)

# Tuples cannot be modified
# data[0] = 100  # This will give an error

# -------------------------------
# 9. Simple Practice Task
# -------------------------------
# Find sum of list elements
total = 0
for num in numbers:
    total += num

print("Sum of list:", total)
