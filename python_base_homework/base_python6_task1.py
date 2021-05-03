# Даны две строки. Выведите на экран символы, которые есть в обоих строках.


str1 = 'Hello! What are you doing?'
str2 = 'Hi! I don`t know yet. Good by.'


def create_set(some_str):
    set_of_symbols = set()
    for symbol in some_str:
        set_of_symbols.add(symbol)
    return set_of_symbols


str_set1 = create_set(str1)
str_set2 = create_set(str2)
new_str_set = str_set1.intersection(str_set2)
print(new_str_set)
