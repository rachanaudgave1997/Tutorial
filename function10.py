#Write a Python function to sum all the numbers in a list. 

def sum_numbers(numbers):
    total = 0  
    for num in numbers:
        total += num  
    return total

list = [8, 2, 3, 0, 7]
result = sum_numbers(list)
print("Sum of the numbers:", result) 

 # Output: Sum of the numbers: 20
