import os.path


def check_file():
    path = "base.txt"
    isExist = os.path.exists(path)
    if isExist is True:
        print(f"База данных найдена. Можно продолжать работу")
    else:
        print(f"Файл базы данных не найден!!!! Дальнейшая работа не возможна")
        exit()
