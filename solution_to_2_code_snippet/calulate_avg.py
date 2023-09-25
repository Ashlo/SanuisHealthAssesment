def calculate_average(numbers):
    total = 0
    count = 0  

    for num in numbers:
        total += num
        count += 1  

    if count == 0:  # Check to avoid division by zero
        return 0

    average = total / count  
    return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print(f"The average is: {result}")

