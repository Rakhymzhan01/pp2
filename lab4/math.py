import math
#Write a Python program to convert degree to radian.
def degrees_to_radians(degrees):
    radians = math.radians(degrees)
    return radians

degrees = float(input("Enter degrees: "))
radians = degrees_to_radians(degrees)
print(f"{radians} radians.")

#Write a Python program to calculate the area of a trapezoid.
def trapezoid_area(a, b, h):
    area = 0.5 * (a + b) * h
    return area

a = float(input("Enter the length of the first base (a): "))
b = float(input("Enter the length of the second base (b): "))
h = float(input("Enter the height (h): "))

area = trapezoid_area(a, b, h)
print("The area of the trapezoid is:", area)

#Write a Python program to calculate the area of regular polygon.
def regular_polygon_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

# Test the function
n = int(input("Enter the number of sides of the regular polygon: "))
s = float(input("Enter the length of each side of the regular polygon: "))

area = regular_polygon_area(n, s)
print("The area of the regular polygon is:", area)

#Write a Python program to calculate the area of a parallelogram.
def parallelogram_area(base, height):
    area = base * height
    return area

base = float(input("Enter the length of the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = parallelogram_area(base, height)
print("The area of the parallelogram is:", area)
