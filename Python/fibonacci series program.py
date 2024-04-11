def generate_fibonacci_series(n):
    fibonacci_series = []
    if n <= 0:
        return fibonacci_series
    elif n == 1:
        fibonacci_series.append(0)
        return fibonacci_series
    elif n == 2:
        fibonacci_series.extend([0, 1])
        return fibonacci_series
    else:
        fibonacci_series.extend([0, 1])
        while len(fibonacci_series) < n:
            next_term = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_term)
        return fibonacci_series

# Example: Generate Fibonacci series up to 10 terms
n = 10
fib_series = generate_fibonacci_series(n)
print("Fibonacci series up to", n, "terms:", fib_series)
