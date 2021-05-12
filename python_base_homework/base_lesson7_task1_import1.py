# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
# интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
# замене последнего на другой, взаимодействующий с пользователем иным способом, программа
# должна продолжать корректно работать.
import base_lesson7_task1 as links


def user_actions():
    action = None
    while action != '':
        action = input('Choose your action(a=add link, g=get link, "Enter"=exit): ')
        if action == 'a':
            user_link_name = input('Enter new link name: ')
            user_link = input('Enter your link: ')
            links.add_link(user_link_name, user_link)
        elif action == 'g':
            links.get_link(input('Enter name of the link: '))
        elif action != '':
            print('Wrong action. Try again.\n')


user_actions()
