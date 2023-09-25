def find_maximum(numbers):
    if not numbers:  # Check if the list is empty
        return None

    max_num = numbers[0]  # Initialize to the first number in the list

    for num in numbers:
        if num > max_num:
            max_num = num  # Corrected the assignment here

    return max_num

numbers = [15, 27, 8, 42, 55]
result = find_maximum(numbers)
print(f"The maximum number is: {result}")

