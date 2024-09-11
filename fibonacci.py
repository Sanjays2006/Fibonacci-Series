def generate_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series


try:
    num_terms = int(input("enter the number of terms in the Fibonacci series: "))
    if num_terms <= 0:
        print("enter a positive integer.")
    else:
        fibonacci_series = generate_fibonacci(num_terms)
        print("Fibonacci series:")
        print(fibonacci_series)
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
