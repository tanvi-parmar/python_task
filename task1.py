#1. calculate simplr interest
def calculate_simple_interest():
    print("--- Simple Interest Calculator ---")
    
    # We use float() so the user can enter decimal values
    principal = float(input("Enter the Principal amount: "))
    rate = float(input("Enter the annual Rate of interest (%): "))
    time = float(input("Enter the Time (in years): "))

    # Applying the formula
    simple_interest = (principal * rate * time) / 100

    # Calculating the total amount (Principal + Interest)
    total_amount = principal + simple_interest

    # Displaying the results
    print("\n--- Results ---")
    print(f"Interest Earned: {simple_interest:.2f}")
    print(f"Total Amount (Principal + Interest): {total_amount:.2f}")

# Run the function
calculate_simple_interest()

#2.find maximum of two numbers
# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Comparison logic
if num1 > num2:
    maximum = num1
elif num2 > num1:
    maximum = num2
else:
    maximum = "Both are equal"

print(f"The result is: {maximum}")

#3.print numbers 1 to 5
# Using a for loop to print 1 to 5
for i in range(1, 6):
    print(i)

text = "Python Programming"

# 4) Find length of string
length = len(text)
print(f"1) Length of the string: {length}")

# 5) Print first character (Index 0)
print(f"3) First character: {text[0]}")

# 6) Print last character (Index -1)
print(f"4) Last character: {text[-1]}")

# 7) Take an input from user
user_name = input("7) Please enter your name: ")

# 8) Print a welcome message
print(f"2) Welcome to Python, {user_name}! We are glad you're here.")

# 9) Check positive or negative value
num = float(input("5) Enter a number to check: "))

if num > 0:
    print("   The number is Positive.")
elif num < 0:
    print("   The number is Negative.")
else:
    print("   The number is Zero.")

# 10) Add 3 numbers
print("\n6) Enter three numbers to add them:")
a = float(input("   Enter 1st number: "))
b = float(input("   Enter 2nd number: "))
c = float(input("   Enter 3rd number: "))

total = a + b + c
print(f"   The sum of {a}, {b}, and {c} is: {total}")