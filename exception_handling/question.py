# Write a Python program that accepts a list of numbers and 
# calculates their average. Raise a custom exception if the list is empty.


class EmptyListError(Exception):
    pass

try:
    numbers = [10, 20, 30, 40]

    if len(numbers) == 0:
        raise EmptyListError("List cannot be empty")

    avg = sum(numbers) / len(numbers)

    print("Average:", avg)

except EmptyListError as e:
    print("Error:", e)