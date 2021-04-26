# Напишите программу, которая вводит с клавиатуры последовательность чисел
# и выводит ее отсортированной в порядке возсрастания


def fill_my_list():
    my_list = []
    len_of_list = int(input('Enter the list length: '))
    for i in range(len_of_list):
        i = int(input('Enter some number for the list: '))
        my_list.append(i)
    my_list.sort()
    print(my_list)


fill_my_list()

