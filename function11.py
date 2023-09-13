#Write a Python function to find the maximum of from given 

def find_max(numbers):
    if not numbers:
        return None  

    maximum = numbers[0]  
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
list = [12, 45, 7, 23, 56, 89, 32]
result = find_max(list)
print("The maximum value is:", result)


# Output: 89
