user_input = input("Введите числа, разделенные пробелом: ")
num_list = user_input.split()

num_tuple = tuple(num_list)

print("Список:", num_list)
print("Кортеж:", num_tuple)
