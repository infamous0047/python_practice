import math

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

dis = b**2 - 4*a*c

root1 = (-b + math.sqrt(dis))/(2*a)
root2 = (-b - math.sqrt(dis))/(2*a)
print(root1, root2)
