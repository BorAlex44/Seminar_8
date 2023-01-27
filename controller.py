from datetime import date


def read_file():
    with open('base.txt', 'r', encoding='UTF-8') as data:
        file = data.read()
    print("-------------------------------------------------")
    print(file)
    print("-------------------------------------------------")


def input_data():
    id_str = get_id()
    surname = input("Введите фамилию покупателя - ")
    name = input("Введите имя покупателя -  ")
    order = input("Введите номер заказа (5 цифр): ")
    current_date = date.today()
    product = input("Введите название продукта - ")
    price = input("Введите стоимость продукта: ")
    new_str = f"{id_str}: {surname} {name} {order} {current_date} {product} {price}\n"
    with open('base.txt', 'a', encoding='UTF-8') as file:
        file.write(new_str)


def get_id():
    with open('base.txt', 'r', encoding='UTF-8') as data:
        file = data.read()
        len_id = 1
        if file == '':
            return len_id
        else:
            str_1 = file.split('\n')
            for i in range(len(str_1)):
                if str_1[i] == '':
                    del str_1[i]
            len_id = [(elem.split(':')[0]) for elem in str_1]
            return int(len_id[-1])+1


def edit_pos():
    with open('base.txt', 'r', encoding='UTF-8') as k:
        lines = k.readlines()
        for line in lines:
            print(line, end='')
        while True:
            line_num = int(input('\nВведите номер строки: '))
            if line_num in range(len(lines)+1):
                text = input('Введите текст: ')
                break
            else:
                print('Такой строки нет!')
    with open('base.txt', 'w', encoding='UTF-8') as f:
        for i, line in enumerate(lines, 1):
            if i == line_num:
                f.writelines(text + '\n')
            else:
                f.writelines(line)


def del_str():
    with open('base.txt', 'r', encoding='UTF-8') as k:
        lines = k.readlines()
        for line in lines:
            print(line, end='')
        while True:
            line_num = int(input('\nВведите номер строки: '))
            if line_num in range(len(lines)+1):
                data = date.today()
                text = f"{line_num}: Запись удалена {data}"
                break
            else:
                print('Такой строки нет!')
    with open('base.txt', 'w', encoding='UTF-8') as f:
        for i, line in enumerate(lines, 1):
            if i == line_num:
                f.writelines(text + '\n')
            else:
                f.writelines(line)


def find_str():
    find_num = input("Введите номер записи: ")
    with open('base.txt', 'r', encoding='UTF-8') as data:
        file = data.read()
        str_1 = file.split('\n')
        list_key = []
        list_value = []
        for i in range(len(str_1)):
            if str_1[i] == '':
                del str_1[i]
        for elem in str_1:
            list_key.append(elem.split(':')[0])
            list_value.append(elem.split(':')[1])
        my_dict = dict(zip(list_key, list_value))
        print(my_dict[find_num])

