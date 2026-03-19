# if statement 
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

#if else statement
age = 16 
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

#if elif else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#Nested if statement
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

#practice problems
#finding the largest of three numbers
num1 = 10
num2 = 20
num3 = 30  
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
