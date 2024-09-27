def length(names):
    even_length_names = []
    odd_length_names = []
    
    for name in names:
        if len(name) % 2 == 0:
            even_length_names.append(name)
        else:
            odd_length_names.append(name)
    
    even_length_names.sort()
    odd_length_names.sort()
    
    return even_length_names, odd_length_names

list_1 = ["Alice", "Ivan", "Matvey", "Viktoriya", "Eva"]
list_2 = ["Anna", "Sergey", "Maksim", "Sophia", "Elena"]
list_3 = ["Ruslan", "Nikita", "Valerya", "Mark", "Vasiliy"]

print(length(list_1)) 
print(length(list_2)) 
print(length(list_3))  
