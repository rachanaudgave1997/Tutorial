#Write a Python program to get the sum of a only non-negative integer.


b = [18,22,15,28,-25,-56,88,-43]
sum = 0
for i in b:
    if i >= 0:
        sum += i
print(sum)


#Output:171
