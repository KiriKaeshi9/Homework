#Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
#арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
#чисел и среднее арифметическое чисел из заданного диапазона.


def numbers(*nums, num_1=0, num_2=0, range1=0, range2=0):
    a = sum(nums)/2
    print(a)
    b = (num_1 + num_2)/2
    print(b)
    c = 0
    for i in range(range1, range2+1):
        c += i
    print(c)
    print(c/2)


numbers(2, 3, 7, 12, num_1=9, num_2=13, range1=3, range2=8)
