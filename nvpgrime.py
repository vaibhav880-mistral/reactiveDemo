#!/usr/bin/env python3
"""
Script to print the first 80 prime numbers with 2-second intervals between each.
"""

import time
import math


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(count):
    """Generate the first 'count' prime numbers."""
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def main():
    """Print the first 80 prime numbers with 2-second intervals."""
    primes = generate_primes(80)
    
    for i, prime in enumerate(primes, 1):
        print(f"Prime #{i}: {prime}")
        if i < 80:  # No sleep after the last prime
            time.sleep(2)


if __name__ == "__main__":
    main()
