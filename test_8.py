import random

# Generate a random 4-digit binary number (as a string)
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert the binary number to base 10
decimal_number = int(binary_number, 2)

# Output the results
print(f"Random 4-digit binary number: {binary_number}")
print(f"Decimal equivalent: {decimal_number}")
