# Task 1: Create a while loop to print out numbers less than or equal to 17
print("Task 1: Numbers less than or equal to 17")
count = 0
while count <= 17:
    print(count)
    count += 1  # Increment count to avoid infinite loop

# Task 2: Create a while loop to print out only the odd values less than or equal to 28
print("\nTask 2: Odd numbers less than or equal to 28")
count = 1
while count <= 28:
    if count % 2 != 0:  # Check if the number is odd
        print(count)
    count += 1  # Increment count to move to the next number

# Task 3: Construct a while loop using input from the user as conditional.
# The structure should be count <= the-user-input and make sure it does not run forever!!
print("\nTask 3: User-defined loop with conditional input")
user_input = int(input("Enter a number for the loop to run up to: "))
count = 0
while count <= user_input:
    print(count)
    count += 1  # Increment count to avoid infinite loop
