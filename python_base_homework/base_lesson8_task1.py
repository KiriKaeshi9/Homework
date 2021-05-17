# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
# действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
# сумму.
import random

with open('random_numbers', 'w') as r_n:
    for number in range(10000):
        random_number = random.randint(-100, 100)
        r_n.write('{0} '.format(random_number))


with open('random_numbers', 'r') as r_n:
    list_of_numbers = []
    number_of_file = ''
    numbers_of_file = r_n.read()
    for symbol in numbers_of_file:
        if symbol == ' ':
            list_of_numbers.append(int(number_of_file))
            number_of_file = ''
        else:
            number_of_file += symbol
    print(sum(list_of_numbers))
