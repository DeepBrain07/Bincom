def fibonacci_sum(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    sum_fib = a + b  # Sum of first two Fibonacci numbers

    # Generate the next Fibonacci numbers and sum them up
    for _ in range(2, n):
        a, b = b, a + b
        sum_fib += b

    return sum_fib

# Calculate the sum of the first 50 Fibonacci numbers
n = 50
result = fibonacci_sum(n)

# Output the result
print(f"The sum of the first {n} Fibonacci numbers is: {result}")
