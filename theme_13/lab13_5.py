import numpy as np

# 1: Генерация фиктивных данных
np.random.seed(0)  
num_students = 10 
num_subjects = 5   

first_names = ["Алексей", "Мария", "Сергей", "Анна", "Дмитрий", "Елена", "Иван", "Ольга", "Никита", "Татьяна"]
last_names = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Зайцев", "Васильев", "Соломонов", "Федоров"]

grades = np.random.randint(60, 101, size=(num_students, num_subjects))

# 2: Рассчет среднего балла каждого студента
average_scores = np.mean(grades, axis=1)

# 3: Поиск студента с самым высоким средним баллом
highest_avg_index = np.argmax(average_scores)
highest_avg_student = (first_names[highest_avg_index], last_names[highest_avg_index], average_scores[highest_avg_index])

# 4: Рассчет среднего балла по каждому предмету
average_subject_scores = np.mean(grades, axis=0)

# 5: Поиск предмета с самым высоким средним баллом
highest_subject_index = np.argmax(average_subject_scores)
subjects = ["Математика", "Наука", "Русский язык", "История", "Искусство"]
highest_avg_subject = (subjects[highest_subject_index], average_subject_scores[highest_subject_index])

# 6: Определение, сколько студентов получили оценку выше 80
students_above_80 = np.sum(average_scores > 80)

print("Сгенерированный список студентов и их оценки:")
for i in range(num_students):
    print(f"{first_names[i]} {last_names[i]}: {grades[i]} (средний балл: {average_scores[i]:.2f})")

print(f"\nСтудент с самым высоким средним баллом: {highest_avg_student[0]} {highest_avg_student[1]} (средний балл: {highest_avg_student[2]:.2f})")
print(f"Средние баллы по предметам: {average_subject_scores}")
print(f"Предмет с самым высоким средним баллом: {highest_avg_subject[0]} (средний балл: {highest_avg_subject[1]:.2f})")
print(f"Количество студентов с оценкой выше 80: {students_above_80}")
