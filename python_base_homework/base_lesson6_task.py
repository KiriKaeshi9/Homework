# Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает
# произвольное количество именованных параметров. Вызовите её с созданным словарём и явно
# указывая параметры.


my_dict = {'first': 1, 'second': 2, 'third': 3}


def my_dict_func(**kwargs):
    for key, item in kwargs.items():
        print(key, item)


my_dict_func(first=my_dict['first'], second=my_dict['second'], third=my_dict['third'])



