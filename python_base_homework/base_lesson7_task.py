# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте
# отдельные его имена.


def get_numbers(end_number):
    simple_numbers = []
    for number in range(2, end_number+1):
        i = 1
        while i <= number:
            i += 1
            if number % i == 0 and i != number:
                break
            elif number % i != 0:
                continue
            else:
                simple_numbers.append(number)
    return simple_numbers


list_of_simple_numbers = get_numbers(50)
simple_number1 = list_of_simple_numbers[0]
simple_number2 = list_of_simple_numbers[1]
simple_number3 = list_of_simple_numbers[2]
