#!/usr/bin/env python3
"""
Script to print the first 50 prime numbers with a 2-second interval between each.
"""

import time


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_first_n_primes(n: int = 50, interval: float = 2.0) -> None:
    """Print the first n prime numbers with a specified interval between each."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    for prime in primes:
        print(prime)
        time.sleep(interval)


if __name__ == "__main__":
    print("Printing the first 50 prime numbers with a 2-second interval:")
    print_first_n_primes()
