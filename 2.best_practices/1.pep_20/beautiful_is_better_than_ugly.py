from math import sqrt

side_a = float(input("The length of the 'a' side: "))
side_b = float(input("The length of the 'b' side: "))
hypotenuse = sqrt(side_a**2 + side_b**2)

print("The length of the hypotenuse is", hypotenuse)
