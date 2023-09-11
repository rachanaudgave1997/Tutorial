#n divisible by 2 or 3

n = 10

if n % 2 == 0 and n % 3 != 0:
    print("Divisible by 2, not divisible by 3")
elif n % 3 == 0 and n % 2 != 0:
    print("Divisible by 3, not divisible by 2")
elif n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by 2 and 3")

#Output:Divisible by 2, not divisible by 3