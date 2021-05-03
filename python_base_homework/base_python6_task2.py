# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
# реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
# ссылки по её названию.


def create_links():
    links = dict()
    while True:
        long_link = input('Enter some link: ')
        name_link = input('Enter name of the link: ')
        if long_link == '' or name_link == '':
            break
        links[name_link] = long_link
    return links


def get_links(links):
    while True:
        try:
            choose_link = input('Enter the link name: ')
            if choose_link == '':
                break
            print(links[choose_link])
        except KeyError:
            print('Wrong the link name. Try again')
            continue


dict_of_links = create_links()
print(dict_of_links)
get_links(dict_of_links)



