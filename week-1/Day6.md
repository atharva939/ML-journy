# Day 6 - Functions

## Topics Covered

* Functions
* Parameters
* Return values
* Default arguments
* Lambda functions

---

## What I Learned

### 1. Functions

A function is a reusable block of code that performs a specific task. Functions help reduce code repetition and improve readability.

Syntax:
def function_name():
# code block

---

### 2. Defining and Calling Functions

Example:
def greet():
print("Hello")

greet()

Explanation:

* A function is defined using the def keyword
* The function runs only when it is called

---

### 3. Functions with Parameters

Example:
def greet(name):
print("Hello", name)

greet("Atharva")

Explanation:

* Parameters allow passing values into a function
* Makes the function more flexible and reusable

---

### 4. Return Values

Example:
def add(a, b):
return a + b

result = add(5, 3)
print(result)

Explanation:

* return sends the result back to the caller
* Allows storing the output in a variable

---

### 5. Default Parameters

Example:
def greet(name="User"):
print("Hello", name)

greet()
greet("Atharva")

Explanation:

* A default value is used if no argument is provided

---

### 6. Lambda Functions

Example:
square = lambda x: x * x

Explanation:

* Lambda functions are small, anonymous functions
* Used for simple one-line operations

---

## Code Example

def add(a, b):
return a + b

result = add(2, 3)
print(result)

---

## My Understanding

Functions help organize code into reusable blocks.
They make programs easier to read, maintain, and scale.
Functions are widely used in data processing and machine learning workflows.

---

## Challenges Faced

* Understanding the difference between print and return
* Writing reusable and meaningful functions

---

## Key Takeaways

* Functions reduce repetition in code
* Parameters make functions flexible
* Return is used to get results from functions
* Lambda functions are useful for simple tasks

---

## Next Step

Revise all Python concepts and start a mini project
