def a_grades(grades):
    grades = [grade for grade in grades if grade != 2]
    grades = [4 if grade == 3 else grade for grade in grades]
    return grades

grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

updated_grades1 = a_grades(grades1)
updated_grades2 = a_grades(grades2)
updated_grades3 = a_grades(grades3)

print(f"Обновленный список оценок 1: {updated_grades1}")
print(f"Обновленный список оценок 2: {updated_grades2}")
print(f"Обновленный список оценок 3: {updated_grades3}")
