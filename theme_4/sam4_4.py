def average(*args):  
    if args: 
        result = sum(args) / len(args)  
        print(f"Среднее арифметическое: {result}") 
    else:
        print("Аргументы не переданы")  

if __name__ == '__main__': 
    average(10, 20, 30, 40) 
