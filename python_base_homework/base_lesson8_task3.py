# Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы
# он сохранял базу ссылок на диске и не «забывал» при перезапуске.
import shelve


def add_link():
    try:
        new_link_name = input('Enter new name of the link: ')
        if new_link_name == '' or new_link_name in saved_links.keys():
            raise KeyError
        new_link = input('Enter new link: ')
        if new_link == '':
            raise KeyError
        else:
            saved_links[new_link_name] = new_link
            print()
    except KeyError:
        print('This link already exists or link name/link is empty. Try again.\n')


with shelve.open('saved_links') as saved_links:
    action = None
    while action != '':
        action = input('Choose your action(a=add link, g=get link, "Enter"=exit): ')
        if action == 'a':
            add_link()
        elif action == 'g':
            link_name = input('Enter the link name: ')
            print(saved_links.get(link_name, 'This link does not exists. Try again.'))
            print()
        elif action != '':
            print('Incorrect action. Try again.\n')
