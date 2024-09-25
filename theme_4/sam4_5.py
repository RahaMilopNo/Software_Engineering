from triangle_area import heron_area  

def main():
    print("Введите длины сторон треугольника:")
    a = float(input("Сторона a: "))  
    b = float(input("Сторона b: "))  
    c = float(input("Сторона c: "))  

    area = heron_area(a, b, c)

    print(f"Площадь треугольника: {area}")

if __name__ == '__main__':  
    main()  