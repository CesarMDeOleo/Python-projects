side1 = 0
side2 = 0 
hypotenuse = 0


for side1 in range(1, 1001):
    for side2 in range(side1,1001):
        for hypotenuse in range(side2,1001):
            if (hypotenuse**2 == side1 ** 2 + side2 ** 2):
                print (f'Side 1: {side1} | Side 2: {side2} | Hypotenuse: {hypotenuse}')
            elif (hypotenuse > 1000):
                break
