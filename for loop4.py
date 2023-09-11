#cubes of odd number :

cube=[]
for i in range(20,40):
    if i%2 !=0:
        cube.append(i**3)
print(cube)


#Output:[9261, 12167, 15625, 19683, 24389, 29791, 35937, 42875, 50653, 59319]
