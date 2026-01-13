# 1.print message
print("HEllO WORLD")

#2. add two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)

#3. even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

#4. check leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

    
#5. print PI value
import math

print("The value of PI is:", math.pi)

#6. store and print constant value
PI = 3.14159
MAX_USERS = 100

    print("The value of PI is:",PI)
    print("The maximum allowed users:",MAX_USERS)

#7.square of a number
number = int(input("Enter a number to square: "))
square = number ** 2
print(f"The square of {number} is {square}")

#8. area of circle
# Define Pi as a constant
PI = 3.14159
radius = float(input("Enter the radius of the circle: "))
area = PI * (radius ** 2)
print(f"The area of the circle is: {area}")

#9.check data type
my_number = 10
my_decimal = 5.5
my_text = "Hello"
my_boolean = True
print(f"Data: {my_number} | Type: {type(my_number)}")
print(f"Data: {my_decimal} | Type: {type(my_decimal)}")
print(f"Data: {my_text} | Type: {type(my_text)}")
print(f"Data: {my_boolean} | Type: {type(my_boolean)}")

#10.use math function
import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"4 to the power of 3: {math.pow(4, 3)}")
print(f"Round 4.2 up: {math.ceil(4.2)}")    
print(f"Round 4.7 down: {math.floor(4.7)}") 
print(f"The value of Pi: {math.pi}")
print(f"The value of Euler's number (e): {math.e}")
angle = math.radians(90)
print(f"Sine of 90 degrees: {math.sin(angle)}")

#11. find power
import math
result = math.pow(5, 4)
print(f"10 to the power of 4 is: {result}")

#12.check positive or negative number

number = float(input("Enter a number: "))

if number > 0:
    print("This is a Positive number.")
elif number < 0:
    print("This is a Negative number.")
else:
    print("The number is Zero.")
