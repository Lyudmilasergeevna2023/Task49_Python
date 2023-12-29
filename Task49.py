from csv import DictReader, DictWriter
from os.path import exists
class LenNumberError:
    def __init__(self, txt):
        self.txt = txt

class LenNameError:
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise LenNameError("Таких имён нет")
            else:
                is_valid_first_name = True
        except ValueError:
            print("Невалидное имя")
            continue
        except LenNameError as err:
            print(err)
            continue
    last_name = 'Ivanov'
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Невалидная длина")
            else:
                is_valid_number = True
        except ValueError:
            print("Невалидный номер")
            continue
        except LenNumberError as err:
            print(err)
            continue
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print("Такой пользователь уже существует")
            return
    obj = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def main():
    while True:
        command = input('Ведите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            #print('Файл создан')
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан. Создайте файл.')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            pass

main()
