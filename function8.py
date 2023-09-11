
#create user define function to create list for specific range

def create_range_list(start, end):
    my_list = list(range(start, end + 1))
    return my_list

start_value = 5
end_value = 15
result_list = create_range_list(start_value, end_value)
print(result_list)

#Output:[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]








