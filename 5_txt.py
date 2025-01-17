import pandas as pd
import numpy as np
import statistics

# Make a program that reads words from a file line by line

words = []

with open("sample.txt", "r") as file:
    for line in file:
        words_in_line = line.strip().split()
        for word in words_in_line:
            words.append(word)

words_sorted = sorted(words, key=len, reverse=True)
print(words_sorted)

with open("written.txt", "w") as file:
    for word in words_sorted:
        file.write(word + "\n")
        