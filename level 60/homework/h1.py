def repeats(arr):
    return sum(x for x in arr if arr.count(x) == 1)



import re

def sum_of_integers_in_string(s):
    return sum(map(int, re.findall(r'\d+', s)))



def find_missing_number(numbers):
    return sum(range(numbers[0], numbers[-1] + 1)) - sum(numbers)
