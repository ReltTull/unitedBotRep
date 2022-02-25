import os.path
"""
Метод is_there_file проверяет существует ли файл

"""


def is_there_file(name_id):
    element = os.path.isfile(f'{name_id}.csv')
    return element


"""
Метод add_log создает и дописывает файл по id
В файл записывается:  остаток конфет/ общее кол-во конфет/ максимальное кол-во за ход/ сделал игрок ход или нет

"""

def add_log(name, keep, candies = 300, max_bet = 14):
    key = 0
    if not is_there_file(name):
        with open(f'{name}.csv', 'a+', encoding='utf8') as data:
            data.write(f'{keep}, {candies}, {max_bet}, {key}; ')
    else:
        your_last_move = last_move(name)
        if your_last_move == '0':
            key = 1
            if keep == 0:
                with open(f'{name}.csv', 'a+', encoding='utf8') as data1:
                    data1.write(f'{keep}, {candies}, {max_bet}, {key}\n')
            else:
                with open(f'{name}.csv', 'a+', encoding='utf8') as data2:
                    data2.write(f'{keep}, {candies}, {max_bet}, {key}; ')
        else:
            key = 0
            if keep == 0:
                with open(f'{name}.csv', 'a+', encoding='utf8') as data1:
                    data1.write(f'{keep}, {candies}, {max_bet}, {key}\n')
            else:
                with open(f'{name}.csv', 'a+', encoding='utf8') as data2:
                    data2.write(f'{keep}, {candies}, {max_bet}, {key}; ')


"""
Метод last_move

"""

def last_move(name_id):
    with open(f'{name_id}.csv', 'r', encoding='utf8') as my_file:
        f = my_file.read()
        f = f.split('\n')
        if f[-1] == '':
            t = f[-2]
            return t[-3]
        else:
            t = f[-1]
            return t[-3]


add_log('S2022', 4)
last_move('S2022')





