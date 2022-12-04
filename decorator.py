#Проверка слова состоит ли из англисских букв алфавита

import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        self.lang = string.ascii_lowercase
        print(f"Алфавит : {self.lang}")

    def letters_num(self):
        self.letters = string.ascii_lowercase
        print(f"Количество букв в алфавите: {len(self.letters)}")


class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__("En", string.ascii_lowercase)

    @staticmethod
    def __letters_num():
        print(f'Англиский алфавит состоит из: {len(string.ascii_lowercase)} символов')

    def is_en_letter(self, word):
        print(f'Строка: {word}')
        for i in word:
            if i in string.ascii_lowercase:
                print(f'"Строка: {i} пренадлежит англискому алфавиту"')
            elif i in string.ascii_uppercase:
                print(f'"Строка: {i} пренадлежит англискому алфавиту"')
            else:
                print(f'"Строка: {i} не пренадлежит англискому алфавиту"')

    def letters_num(self):
        self.__letters_num()

    @staticmethod
    def Example():
        Example_1 = "Hello world"
        print(f'Пример текстa: {Example_1}')


if __name__ == '__main__':
    st = EngAlphabet()
    st.print()
    st._EngAlphabet__letters_num()
    st.is_en_letter("F")
    st.is_en_letter("Щ")
    st.Example()
