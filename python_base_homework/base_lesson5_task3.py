# Напишите программу, которая вводит с клавиатуры текст и
# выводит отсортированные по алфавиту слова данного текста.


def words():
    text = input('Enter some text: ')
    text = text.lower()
    list_of_words = []
    word = ''
    for symbol in text:
        if symbol.isalpha():
            word += symbol
        else:
            if word.isalpha():
                list_of_words.append(word)
            word = ''
    if text[-1].isalpha():
        list_of_words.append(word)
    list_of_words.sort()
    print(list_of_words)


words()
