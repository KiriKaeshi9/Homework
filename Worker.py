class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def working_day(self, day):
        if 1 <= day <= 5:
            print('The worker', self.name + ',', self.age, 'years old, is going to work today.')
        elif 7 >= day > 5:
            print('The worker', self.name + ',', self.age, 'years old, is not going to work today.')
        else:
            print('It`s not a day of the week. Choose from 1 to 7.')


John = Worker('John', 30)
Jane = Worker('Jane', 26)
Hideo = Worker('Hideo', 40)

John.working_day(4)
Jane.working_day(6)
Hideo.working_day(9)

