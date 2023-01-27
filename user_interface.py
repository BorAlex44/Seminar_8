from check_mod import check_file
from controller import read_file, input_data, edit_pos, del_str, find_str


def user_menu():
    check_file()
    while True:
        user_input = input('Введите номер меню:\n'
                           '1 - показать все записи\n'
                           '2 - найти запись\n'
                           '3 - добавить запись\n'
                           '4 - редактировать запись\n'
                           '5 - удалить запись\n'
                           '6 - выход\n')

        match user_input:
            case '1':
                read_file()
            case '2':
                find_str()
            case '3':
                input_data()
            case '4':
                edit_pos()
            case '5':
                del_str()
            case '6':
                break
            case _:
                print('The menu item is not recognized. Try again!')
