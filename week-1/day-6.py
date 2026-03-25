# Day 6 - Functions Practice

# -------------------------------
# 1. Simple Function
# -------------------------------
def greet():
    print("Hello")

greet()

# -------------------------------
# 2. Function with Parameter
# -------------------------------
def greet_user(name):
    print("Hello", name)

greet_user("Atharva")

# -------------------------------
# 3. Function with Return Value
# -------------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# -------------------------------
# 4. Even or Odd Function
# -------------------------------
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", check_even_odd(10))

# -------------------------------
# 5. Find Maximum
# -------------------------------
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", find_max(10, 20))

# -------------------------------
# 6. Factorial Function
# -------------------------------
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial:", factorial(5))

# -------------------------------
# 7. Default Parameter
# -------------------------------
def greet_default(name="User"):
    print("Hello", name)

greet_default()
greet_default("Atharva")

# -------------------------------
# 8. Lambda Function
# -------------------------------
square = lambda x: x * x
print("Square:", square(5))

# -------------------------------
# 9. Practice Task
# -------------------------------
# Function to calculate sum of list

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = [1, 2, 3, 4, 5]
print("Sum of list:", sum_list(nums))
