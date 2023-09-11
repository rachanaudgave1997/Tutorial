
#create list 20-1 (reverse order) using while loop

numbers = []
i = 20

while i >= 1:
    if i % 4 == 0:
        # Using the 'break' statement to exit the loop when we encounter a number divisible by 4
        break
    elif i % 5 == 0:
        # Using the 'continue' statement to skip numbers divisible by 5
        i -= 1
        continue
    else:
        # Using the 'pass' statement for all other numbers
        pass
    
    numbers.append(i)
    i -= 1

print(numbers)




#Output:[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]