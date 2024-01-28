#!/usr/bin/env python3

import sys


def factorize_number(n):
    # Find the smallest factor (starting from 2)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1


def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor1, factor2 = factorize_number(number)
            print(f"{number}={factor1}*{factor2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        factorize_file(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Please make sure all lines are valid natural numbers.")
        sys.exit(1)
