# Task 1: Create a for loop to print out numbers between 0 and 15.
# The loop should stop when the number 10 is encountered.
print("Task 1: Numbers between 0 and 15, stopping at 10")
for i in range(16):
    if i == 10:
        break  # Stop the loop when the number 10 is reached
    print(i)

# Task 2: Create a for loop to print out only the odd values between 0 and 18.
# The loop should stop when the number is 12.
print("\nTask 2: Odd numbers between 0 and 18, stopping at 12")
for i in range(0, 19, 2):  # Loop through odd numbers by using a step of 2
    if i == 12:
        break  # Stop the loop when the number 12 is reached
    print(i)

# Task 3: Construct a for loop using input from the user as conditional.
# The loop should stop when the number is half the range specified.
print("\nTask 3: User-defined range with stopping condition")
user_input = int(input("Enter a number for the loop to run up to: "))
half_range = user_input // 2  # Calculate half of the range (integer division)
for i in range(user_input + 1):  # Loop from 0 to user_input
    if i == half_range:
        break  # Stop the loop when the number is half the range
    print(i)
