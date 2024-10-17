def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content: 
                raise ValueError("файл пустой")
            print(content)
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден")

if __name__ == '__main__':
    read_file('empty_file.txt')
    read_file('info_file.txt')
