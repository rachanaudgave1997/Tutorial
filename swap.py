#Given a list, write a Python code  to swap first and last element of the list:

list = [1, 2, 3, 4, 5,6]
if len(list) >= 2:
    list[0], list[-1] = list[-1], list[0]
print(list)


#Output:[6,5, 2, 3, 4, 1]
