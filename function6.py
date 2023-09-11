
#create user define function sum of even numbers

def sum_even_numbers(numbers):
    result = 0
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            result += number
    return result

values = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum_even_numbers(values)
print(result)


#Output:20





