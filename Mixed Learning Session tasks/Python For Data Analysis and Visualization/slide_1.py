# Task 1: Create the lists
int_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
range_list = list(range(100))
fruit_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]
mixed_list = ["Student Name: John", "ID: 12345", "Grade: A", "Pass: Yes"]

# Task 2: Extend the list of 10 integers by 1 element and then 5 elements
int_list.append(110)  # Add 1 element
int_list.extend([120, 130, 140, 150, 160])  # Add 5 elements

# Task 3: Delete the last 50 numbers of the range list
del range_list[-50:]

# Task 4: Extend the list of fruits by adding some others (min. 5 fruits)
fruit_list.extend(["papaya", "pear", "peach", "plum", "pomegranate"])

# Task 5: Extend the 10 integer list by adding the fruits list elements
int_list.extend(fruit_list)

# Display the results
print("List of integers:", int_list)
print("Range list:", range_list)
print("Fruit list:", fruit_list)
print("Mixed list:", mixed_list)
