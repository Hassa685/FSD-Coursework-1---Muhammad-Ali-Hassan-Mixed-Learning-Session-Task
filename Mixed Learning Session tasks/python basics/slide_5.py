import math

# Task 1: Create a function that prints out the average of 3 numbers
def average_of_three(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print(f"The average of {num1}, {num2}, and {num3} is {average}")

# Task 2: Create a function that will print out the sum of 5 numbers
def sum_of_five(num1, num2, num3, num4, num5):
    total_sum = num1 + num2 + num3 + num4 + num5
    print(f"The sum of {num1}, {num2}, {num3}, {num4}, and {num5} is {total_sum}")

# Task 3: Create a function to solve the quadratic equation: ax^2 + bx + c = 0
# The function will print out the two solutions of the equation.
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real and different roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots of the equation are {root1} and {root2}")
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        print(f"The root of the equation is {root}")
    else:
        # No real roots (complex roots)
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The roots of the equation are {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

# Example calls
average_of_three(5, 10, 15)
sum_of_five(1, 2, 3, 4, 5)
solve_quadratic(1, -3, 2)  # Example for quadratic: x^2 - 3x + 2 = 0
