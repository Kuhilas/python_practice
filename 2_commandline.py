import numpy as np
import statistics
import argparse

# Parser practice. Create similar program to exercise 1. but take the input from command line. I have used sys.argv before so testing parser

# Create parser and set it up for numbers
parser = argparse.ArgumentParser(description="Store numbers in a list")

parser.add_argument("numbers", nargs="+", type=int, help="List of numbers")

args = parser.parse_args()

numbers = args.numbers


# Running the same end as in program 1.

numbers_min = min(numbers)
numbers_max =  max(numbers)

numbers_mean = np.mean(numbers)
numbers_median = np.median(numbers)
numbers_mode = statistics.mode(numbers)

print()
print(f"Highest number was: {numbers_max} and the lowest: {numbers_min}")
print()
print(f"Mean: {numbers_mean}\n Median: {numbers_median}\n Mode: {numbers_mode}\n")