#!/usr/bin/env python3
"""
Script to print the first 50 prime numbers with 2-second intervals between each.
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
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes_with_delay(count=50, delay_seconds=2):
    """Print the first 'count' prime numbers with 'delay_seconds' interval."""
    primes_found = 0
    num = 2
    
    print(f"Printing the first {count} prime numbers with {delay_seconds}-second intervals:")
    print("-" * 60)
    
    while primes_found < count:
        if is_prime(num):
            print(f"Prime #{primes_found + 1}: {num}")
            primes_found += 1
            if primes_found < count:  # Don't sleep after the last prime
                time.sleep(delay_seconds)
        num += 1
    
    print("-" * 60)
    print(f"Completed! Printed {count} prime numbers.")


if __name__ == "__main__":
    print_primes_with_delay(count=50, delay_seconds=2)
