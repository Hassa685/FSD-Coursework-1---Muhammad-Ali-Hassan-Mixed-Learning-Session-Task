# Task 1: Using continue, create a while loop to print out numbers less than or equal to 9
# except those that are not divisible by 2 (i.e., print only even numbers).
print("Task 1: Even numbers between 0 and 9 (excluding odd numbers)")
count = 0
while count <= 9:
    if count % 2 != 0:  # If the number is odd, skip the iteration
        count += 1
        continue
    print(count)
    count += 1

# Task 2: Using continue, create a while loop to print out only the even values less than or equal to 16
# Hint: use a conditional statement with modulo to check if the number is even.
print("\nTask 2: Even numbers less than or equal to 16")
count = 0
while count <= 16:
    if count % 2 != 0:  # If the number is odd, skip the iteration
        count += 1
        continue
    print(count)
    count += 1
