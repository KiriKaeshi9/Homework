class Alphabet:
    language = 'English'
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    def list_of_letters(self):
        for i in self.alphabet:
            if i != self.alphabet[-1]:
                print(i, end=', ')
            else:
                print(i)

    def number_of_letters(self):
        print(len(self.alphabet))


al = Alphabet()
al.list_of_letters()
al.number_of_letters()
