# Task 1: Create a for loop that will print out numbers from 0-10
print("Task 1: Numbers from 0 to 10")
for i in range(11):
    print(i)

# Task 2: Create a for loop that will print out only the even values between 0-10
print("\nTask 2: Even numbers between 0 and 10")
for i in range(11):
    if i % 2 == 0:  # Check if the number is even
        print(i)

# Task 3: Construct a for loop using range. You must specify the range as an input from the user.
print("\nTask 3: User-defined range")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Printing numbers from {start} to {end}:")
for i in range(start, end + 1):
    print(i)

# Task 4: Construct another for loop by taking all range inputs from the user: start, end, and step
print("\nTask 4: User-defined range with start, end, and step")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step value: "))

print(f"Printing numbers from {start} to {end} with a step of {step}:")
for i in range(start, end + 1, step):
    print(i)
