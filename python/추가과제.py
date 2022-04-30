import math

# 1번
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
a, b = divmod(num1, num2)
print("몫:", a)
print("나머지:", b)

# 2번
x = int(input("Enter a value for x: "))
result = 3*x**5 + 2*x**4 - 5*x**3 - x**2 + 7*x - 6
print("Polynomial for x =", x,":", result)

# 3번
n = int(input("Enter the number of people: "))
p = 1 - math.factorial(365)/((365**n)*math.factorial(365-n))
print(100*p)