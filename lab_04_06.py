# Создайте класс HammingEncoder, конструктор которого принимает на вход количество
# информационных разрядов dataBits, на основе которых рассчитывает значение количества
# контрольных разрядов – controlBits. dataBits и controlBits являются атрибутами класса.
# Реализуйте метод encode(str), служащий для кодирования строки двоичных символов str с
# использованием кода Хэмминга с установленными параметрами dataBits и controlBits.
# Реализуйте метод decode(str), служащий для определения кода ошибки закодированной строки str.

class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        self.controlBits = self.calculate_cbits()

    def calculate_cbits(self):
        x = 2
        m = 2**x-self.dataBits - 1
        while m < x:
            x += 1
            m = 2**x-self.dataBits - 1
        return x

    def make_block(self, s):
        st = ""
        j = 0
        for i in range(1, self.controlBits+self.dataBits+1):
            if i & (i - 1) == 0: # если является степенью 2
                st = st + '0'
            else:
                st = st + s[j]
                j += 1
        return st

    def set_control_bits(self, list1):
        # первый контрольный бит считаем отдельно
        # контрольные биты высчитываются независимо от того, что стоит в самом контрольном бите (0 или 1)
        p = 0
        for i in range(2, self.controlBits + self.dataBits, 2):
            p ^= list1[i]
        list1[0] = p
        for i in range(1, self.controlBits):
            p = 0
            j = m = 2**i - 1  # вычисляемый контрольный бит
            k = 0
            while k < m and j < self.controlBits + self.dataBits -1:
                k += 1
                j += 1
                p ^= list1[j]
            list1[m] = p
            j += 2**i + 1
            while j < self.controlBits + self.dataBits:
                p ^= list1[j]
                k = 0
                while k < m and j < self.controlBits + self.dataBits-1:
                    k += 1
                    j += 1
                    p ^= list1[j]
                j += 2**i+1
            list1[m] = p
        mystr = ""
        for x in range(len(list1)):
            mystr = mystr + str(list1[x])
        return mystr

    def encode(self, s):
        s = self.make_block(s)
        mylist = list()
        for i in range(len(s)):
            mylist.append(int(s[i]))
        s = self.set_control_bits(mylist)
        return s


    def decode(self, s):
        mylist = list()
        for i in range(self.dataBits+self.controlBits):
            mylist.append(int(s[i]))
        mystr = self.set_control_bits(mylist)
        print ("decoded:", mystr)
        position = 0
        for i in range(self.dataBits+self.controlBits):
            if mystr[i] != s[i]:
                position += i + 1
        return position

my_str = '0100010000111101'
# 0100010000111101
ham = HammingEncoder(len(my_str))


str_ec = ham.encode(my_str)
print ("encoded:", str_ec)
osh = "100110000110001011101"
str_dc = ham.decode(osh)
print ("error at position:", str_dc)