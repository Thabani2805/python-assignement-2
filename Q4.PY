import random

# Generate 5 random floating-point numbers between 0 and 10
numbers = [random.uniform(0, 10) for i in range(5)]

# Display the numbers
print("Random numbers:", numbers)

# Find minimum and maximum values
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))