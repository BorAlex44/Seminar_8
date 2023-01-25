from datetime import date


def read_file():
    with open('base.txt', 'r', encoding='UTF-8') as data:
        file = data.read()
    print()
    print(file)
    print()


def input_data():
    id_str = get_id()
    surname = input("Введите фамилию покупателя - ")
    name = input("Введите имя покупателя -  ")
    order = int(input("Введите номер заказа (5 цифр): "))
    current_date = date.today()
    product = input("Введите название продукта - ")
    price = int(input("Введите стоимость продукта: "))
    new_str = f"{id_str}: {name} {surname} {order} {current_date} {product} {price}\n"
    with open('base.txt', 'a', encoding='UTF-8') as file:
        file.write(new_str)


def get_id():
    with open('base.txt', 'r', encoding='UTF-8') as data:
        file = data.read()
        str_1 = file.split('\n')
        for i in range(len(str_1)):
            if str_1[i] == '':
                del str_1[i]
        len_id = len([(elem.split(':')[0]) for elem in str_1])
    return len_id + 1
