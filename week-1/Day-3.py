#for loops
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

#while loop
x = 0
while x < 4:
    print(x)
    x += 1  
  
#break
x = 0
for index in range(10):
    x = index * 10
    if index == 5:
    	break
    print(x)

#Continue
  for index in range(3, 8): 
    x = index * 10
    if index == 5:
    	continue
    print(x)

#Practice
# Multiplication table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
