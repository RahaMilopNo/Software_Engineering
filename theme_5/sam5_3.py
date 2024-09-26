import math

def heron_area(a, b, c):
    s = (a + b + c) / 2 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  
    return area

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_a = min(one)
min_b = min(two)
min_c = min(three)
max_a = max(one)
max_b = max(two)
max_c = max(three)

min_triangle_area = heron_area(min_a, min_b, min_c)
max_triangle_area = heron_area(max_a, max_b, max_c)

print(f"Площадь треугольника из минимальных значений: {min_triangle_area}")
print(f"Площадь треугольника из максимальных значений: {max_triangle_area}")
