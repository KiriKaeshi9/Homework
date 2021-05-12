# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
# интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
# замене последнего на другой, взаимодействующий с пользователем иным способом, программа
# должна продолжать корректно работать.
list_of_links = dict()


def add_link(link_name, link):
    new_link = dict()
    if link_name not in list_of_links.keys() and link_name != '' and link != '':
        new_link[link_name] = link
        print()
        return list_of_links.update(new_link)
    else:
        print('Link with this name exists or link name(link) is empty. Try again.\n')


def get_link(link_name):
    try:
        print(list_of_links[link_name], '\n')
    except KeyError:
        print('Link with this name does not exist. Try again.\n')
