
#create user define function for calculate any given values

def calculate_variance(*values):
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    return variance

result = calculate_variance(1, 2, 5, 6, 8)
print(result)


#Output:8.3





