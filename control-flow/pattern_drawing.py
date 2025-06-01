# pattern_drawing.py

# Prompt user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use while loop to iterate through each row
while row < size:
    # For loop to print asterisks for each column in the current row
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1
