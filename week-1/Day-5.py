# Day 5 - Sets and Dictionaries Practice

# 1. Sets Basics
numbers = {1, 2, 3, 3, 4}
print("Set (duplicates removed):", numbers)

# 2. Adding Elements
numbers.add(5)
print("After adding 5:", numbers)

# 3. Removing Elements
numbers.remove(2)
print("After removing 2:", numbers)

# 4. Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)

# 5. Dictionaries Basics
student = {
    "name": "Atharva",
    "age": 20,
    "course": "AI & DS"
}

print("Student Data:", student)

# 6. Accessing Values
print("Name:", student["name"])

# 7. Updating Values
student["age"] = 21
print("Updated Age:", student)

# 8. Adding New Key
student["city"] = "Nagpur"
print("After adding city:", student)

# 9. Removing Key
student.pop("course")
print("After removing course:", student)

# 10. Looping Through Dictionary
print("Student Details:")
for key, value in student.items():
    print(key, ":", value)

# 11. Practice Task
# Count unique numbers using set

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)

print("Original list:", nums)
print("Unique values:", unique_nums)
print("Count of unique values:", len(unique_nums))
