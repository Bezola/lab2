#  Натуральные числа, содержащие хотя бы одну цифру, введенную с клавиатуры. Данную цифру выводить прописью.

import re

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
slovar = {

    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}


def num_to_text(number):
    return slovar[number]


# -----------------------Введение проверочных цифр-----------------------

control_line = str(input('Введите цифры: '))
control_line = re.sub('\D', '', control_line)
control_num = []
for i in range(len(control_line)):
    control_num.append(control_line[i])

print('-------')

# -----------------------Введение проверяемых чисел---------------------

with open('data_list.txt', 'r') as f:
    lines = f.readlines()
    data = ' '
    for i in lines:
        i = re.sub('\n', ' ', i)
        data += i
    data += ' '

# -----------------------Удаление всего кроме чисел---------------------

data = re.sub('\d*[^\d\s]\S*\s', '', data)

check_list = ''
for i in control_num:
    check_list += i

# -------------------Проверка на наличие введеных чисел-----------------

data = re.sub('\s', '  ', data)
temp = '\s[^' + re.escape(check_list) + '\s]{1,}\s'
data = re.sub(temp, '', data)
data = re.sub('\s{2,}', ' ', data)

# ----------------------------Замена на пропись-------------------------

for check_num in control_num:
    data = re.sub(check_num, num_to_text(check_num), data)

# ----------------------------------Вывод-------------------------------

answer = data.split()
for text in answer:
    print(text)
