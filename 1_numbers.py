import numpy as np
import statistics

#Program that takes as many number as the user wants as input. When ending program prints the min, max, mean, median and mode.

user_input = input("Enter comma-separated numbers: ")
try:
    numbers = [int(x.strip()) for x in user_input.split(',')]

    numbers_min = min(numbers)
    numbers_max =  max(numbers)

    numbers_mean = np.mean(numbers)
    numbers_median = np.median(numbers)
    numbers_mode = statistics.mode(numbers)

    print()
    print(f"Highest number was: {numbers_max} and the lowest: {numbers_min}")
    print()
    print(f"Mean: {numbers_mean}\n Median: {numbers_median}\n Mode: {numbers_mode}\n")

except ValueError:
    print("Invalid input. Please enter numbers separated by commas (Last number should not have a comma).")




