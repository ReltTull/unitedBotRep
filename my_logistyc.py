import os.path
import time


def is_there_file(name_id):
    """Метод is_there_file проверяет существует ли файл"""
    element = os.path.isfile(f'{name_id}.csv')
    return element



def add_log(name, keep, my_list):
    """Метод add_log создает и дописывает файл по id

    Принимает id, остаток конфет, список с условиями игры [кол-во конфет, сколько конфет можно взять за ход, чей ход]"""
    if not is_there_file(name):
        with open(f'{name}.csv', 'a+', encoding='utf8') as data:
            data.write(f'{time.strftime("%Y-%m-%d,%H:%M:%S")},{keep},{my_list};\n')
    else:
        if keep == 0:
            with open(f'{name}.csv', 'a+', encoding='utf8') as data1:
                data1.write(f'{time.strftime("%Y-%m-%d,%H:%M:%S")},{keep},{my_list};\n')
        else:
            with open(f'{name}.csv', 'a+', encoding='utf8') as data2:
                data2.write(f'{time.strftime("%Y-%m-%d,%H:%M:%S")},{keep},{my_list};')



def last_move(name_id):
    """Метод last_move возвращает результаты последнего хода(последняя запись в файле)

       Принимает id  """
    if not is_there_file(name_id):
        return 'Файла нет'
    else:
        with open(f'{name_id}.csv', 'r', encoding='utf8') as my_file:
            f = my_file.read()
            f = f.split('\n')
            if f[-1] == '':
                f.remove(f[-1])
            last_game = f[-1]
            last_game = last_game.split(';')
            if last_game[-1] == '':
                return last_game[-2]
            else:
                return last_game[-1]
