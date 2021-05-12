# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте
# отдельные его имена.
import base_lesson7_task
from base_lesson7_task import simple_number1, simple_number2

new_list_of_simple_numbers = base_lesson7_task.get_numbers(20)
print('Import list: {0}\nNew list: {1}'.format(base_lesson7_task.list_of_simple_numbers, new_list_of_simple_numbers))
print('First simple number: {0}\nSecond simple number: {1}'.format(simple_number1, simple_number2))
