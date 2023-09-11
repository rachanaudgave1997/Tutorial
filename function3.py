
#create user define function for variance of given 5 numbers

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance

values = [5, 7, 8, 9, 10]
result = calculate_variance(values)
print(result)


#Output:3.7





