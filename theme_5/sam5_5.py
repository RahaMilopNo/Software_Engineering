def custom_set(numbers):
    result_set = set()
    number_counts = {}

    for num in numbers:
        if num not in number_counts:
            number_counts[num] = 1
        else:
            number_counts[num] += 1
    
    for num, count in number_counts.items():
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)
    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = custom_set(list_1)
set_2 = custom_set(list_2)
set_3 = custom_set(list_3)

print(f"Множество для list_1: {set_1}")
print(f"Множество для list_2: {set_2}")
print(f"Множество для list_3: {set_3}")
