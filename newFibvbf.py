#!/usr/bin/env python3
"""
Script to print the first 50 Fibonacci numbers with a 2-second interval between each number.
"""

import time

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def print_fibonacci_with_interval():
    """Print the first 50 Fibonacci numbers with 2-second intervals."""
    fib_numbers = fibonacci(50)
    for i, num in enumerate(fib_numbers, 1):
        print(f"Fibonacci({i}): {num}")
        if i < 50:  # No delay after the last number
            time.sleep(2)

if __name__ == "__main__":
    print("Printing first 50 Fibonacci numbers with 2-second intervals...")
    print_fibonacci_with_interval()
    print("Done!")
