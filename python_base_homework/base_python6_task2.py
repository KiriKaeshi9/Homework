# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
# реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
# ссылки по её названию.
dict_of_links = dict()


def create_link(name_link):
    link = dict()
    long_link = input('Enter some link: ')
    link[name_link] = long_link
    return link


def get_link(links):
    choose_link = input('Enter the link name: ')
    return links[choose_link]


while True:
    action = input('Enter your action with a links(a=add, g=get or press "Enter" to exit): ')
    if action == 'a':
        new_link = input('Enter the name of new link: ')
        if new_link not in dict_of_links.keys() and new_link != '':
            dict_of_links.update(create_link(new_link))
            print()
        else:
            print('This link exists.\n')
    elif action == 'g':
        try:
            exist_link = get_link(dict_of_links)
            if exist_link == '':
                raise KeyError
            else:
                print(exist_link, '\n')
        except KeyError:
            print('The link does not exist.\n')
    elif action == '':
        break
    else:
        print('Choose right action.\n')
