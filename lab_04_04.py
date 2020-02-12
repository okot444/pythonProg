
# Создайте класс Encoder, определив для него методы encode() и decode(), аргументом которых
# является строка, а выходными данными – закодированная и декодированная строка соответственно.
# Создайте классы HuffmanEncoder и LZEncoder, унаследованные от класса Encoder, определив для них
# атрибут compressionCoef в конструкторах классов. Для созданных классов HuffmanEncoder и LZEncoder
# переопределите методы encode() и decode(), реализующие кодирование и декодирование поданных
# в качестве аргументов строк, используя методы Хаффмана и Лемпеля-Зива соответственно.
# Определите приватный метод setCompressionCoef() (с использованием двойного подчеркивания),
# осуществляющий расчет коэффициентов сжатия для методов Хаффмана и Лемпеля-Зива в соответствующих
# классах. Метод setCompressionCoef() должен вызываться при работе внутри класса в методе encode().
# Определите общедоступный метод
import math
import operator

class Encoder:
    def encode(self, str):
        pass

    def decode(self, str):
        pass

class HuffmanEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0
        self.d = self.make_dict(string)  # словарь частотный
        self.list_dict = self.sort_list()  # список с частотами букв(упорядоченный по убыванию)

# функция создает список из словаря и сортирует его по убыванию
    def sort_list(self):
        sort_dict = self.d.items()
        lword_sorted = sorted(sort_dict, key=operator.itemgetter(1), reverse=True)
        return lword_sorted

# функция кодирования по Хаффману, на основе словаря ставит соотвествующий двоичный код каждому символу
    def huff_table(self):
        st = ''
        for i in range(len(self.list_dict)):
            st = st + self.list_dict[i][0]
        self.d[st[0]] = '0'  # кодирование Хаффмана
        st = st[1:]
        for i in st:
            self.d[i] = '1'
        for i in st[:len(st) - 1]:  # len(st)-1 : кроме последнего
            self.d[i] += '0'
            for j in st[1:]:
                self.d[j] += '1'
            st = st[1:]

    def make_dict(self, string):
        dct = dict()  # частотный словарь букв
        for letter in string:
            if letter not in dct:
                dct[letter] = 0
            dct[letter] += 1
        return dct

    def encode(self, string):

        self.huff_table()

        string2 = ''
        for i in range(len(string)):
            string2 = string2 + self.d.get(string[i])
        self.__setCompressionCoef()
        return string2

    def decode(self, str):
        self.huff_table()

        new_d = {value: key for key, value in self.d.items()}
        string2 = ''
        #s = fileIn.read()
        # пока не конец строки
        i = 0
        while i < len(str):
            i += 1
            if str[:i] in new_d:
                string2 = string2 + new_d.get(str[:i])
                str = str[i:]
                i = 0
        return string2

    def __setCompressionCoef(self):
        self.compressionCoef = 0


class LZEncoder(Encoder):

    def __init__(self):
        self.compressionCoef = 0

    def search_in_l(self, ch, st, listd):
        ret = 0
        for j in range(ch, len(st) + 1):
            sbst = st[ch:j]
            for i, c in enumerate(listd):
                if sbst == listd[i][0]:
                    ret = c
        return ret

    # k - индекс в строке с которого начинается число
    def number(self, k, st):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ch = st[k]
        i = k
        while st[i + 1] in a:
            i += 1
            ch = st[k:i + 1]
        ch = int(ch)
        return ch

    def encode(self, s):
        listd = [["", "0"]]  # начальное состояние словаря - пустое значение
        # добавить слова в словарь
        k = 0
        n = len(s)
        mystring = ''
        while k < n:
            p = self.search_in_l(k, s, listd)
            l = len(p[0])

            if k + l < n:
                # закодированная строка будет содержать пару (число, символ), поэтому если символ будет
                # представляться цифрой, пару необходимо разграничить (в данном случае разделено символом "~")
                listd.append([p[0] + s[k + l], str(listd.index(p))+ "~" + s[k + l]])
                mystring = mystring + listd[-1][-1]  # слово новое, только что было добавлено в listd
            else:
                mystring = mystring + p[1]  # слово уже есть в словаре
            k += l + 1

        self.__setCompressionCoef()
        return mystring

    def decode(self, s):
        listd = [["", "0"]]
        # считать число
        n = len(s)
        k = 0
        mystring = ''
        while k < n:
            ch = self.number(k, s)
            if ch > listd.index(listd[-1]):
                return False
            k += len(str(ch))
            q = s[k + 1]  # q=st[k]
            k += 2  # k+=1
            listd.append([listd[ch][0] + q, str(ch) + q])
            mystring = mystring + (listd[ch][0] + q)
            #fileOut.write(listd[ch][0] + q)
        return mystring

    def __setCompressionCoef(self):
        self.compressionCoef = 0

string = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991."
huffman = HuffmanEncoder()
encoded = huffman.encode(string)
print(encoded)
decoded = huffman.decode(encoded)
print(decoded)


lz = LZEncoder()
encoded = lz.encode(string)
print(encoded)
decoded = lz.decode(encoded)
print(decoded)