#Define a function that accepts lowercase words and returns uppercase words.

import itertools

def count_combinations(elements):
    combinations = list(itertools.combinations(elements, 2))  
    return len(combinations)

# Example usage:
input_elements = ['a', 'b', 'c']
result = count_combinations(input_elements)
print("Total number of combinations:", result)



# Output:Result is = STATISTICS
