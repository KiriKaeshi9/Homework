# Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными
# файлами.
import random
import pickle
with open('byte_random_numbers', 'wb') as b_rn:
    list_of_numbers = []
    for number in range(10000):
        random_number = random.randint(-100, 100)
        list_of_numbers.append(random_number)
    pickle.dump(list_of_numbers, b_rn)

with open('byte_random_numbers', 'rb') as b_rn:
    print(sum(pickle.load(b_rn)))
