
#create user define factorial function

def factorial(n):
    if n == 0:
        return 1  
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

n = 5
result = factorial(n)
print(f"{n}! = {result}")


#Output:5! = 120





