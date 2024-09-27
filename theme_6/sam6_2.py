def removeFO(tup, value):
    temp_list = list(tup)

    if value in temp_list:
        temp_list.remove(value)
    
    return tuple(temp_list)

print(removeFO((1, 2, 3), 1))         
print(removeFO((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))  
print(removeFO((2, 4, 6, 6, 4, 2), 9))  
