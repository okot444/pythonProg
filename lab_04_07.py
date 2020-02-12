import collections


class Row:
    count = 0

    def __init__(self, collection, value):
        Row.count += 1
        self.id = Row.count
        self.collection = collection.copy()
        self.value = value

class Table:
    def __init__(self, rowsNum):
        self.rowsNum = rowsNum
        self.rows = list()

    # Добавление строки (объект row класса Row) в список.
    # Если в списке уже находится строка с таким же идентификатором,  выдаётся ошибка.
    def addRow(self, row):
        # копия объекта
        c_row = Row(row.collection, row.value)
        c_row.id = row.id
        for i in range(self.rowsNum):
            if self.rowsNum:
                if row.id == self.rows[i].id:
                    print ('id exists')
                    return False
        self.rowsNum += 1
        self.rows.insert(c_row.id, c_row)
        Row.count -= 1

    # Изменение строки (объект row класса Row).
    # Если в списке нет строки с таким же идентификатором, выдаётся ошибка.
    def setRow(self, row):
        for i in range(self.rowsNum):
            if row.id == self.rows[i].id:
                self.rows[i].collection = row.collection.copy()
                self.rows[i].value = row.value
                return

        return False

    # Получение строки c идентификатором rowId. Возвращается объект класса Row.
    def getRow(self, rowId):
        for i in range(self.rowsNum):
            if self.rows[i].id == rowId:
                c_row = Row(self.rows[i].collection, self.rows[i].value)
                c_row.id = self.rows[i].id
                return c_row

    def display(self):
        print("{:^4}".format('id'), end="")
        for i in range(len(self.rows[0].collection)):
            print("{}{} ".format("x", i), end="")
        print("{:^12}".format('f(x1,x2)'))

        for i in range(self.rowsNum):
            print("{:^3}".format(self.rows[i].id), end="")
            for j in range(len(self.rows[i].collection)):
                print("{:^3}".format(self.rows[i].collection[j]), end="")
            print(" |{:^10}".format(self.rows[i].value))


class LogicFunction:
    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum
        self.table = table

    # возвращает список, где функция = 1 (value = 1 в таблице)
    def function1(self):
        table = list()
        for i in range(self.table.rowsNum):
            if self.table.rows[i].value == 1:
                table.append(self.table.rows[i].collection)
        return table

    def minimization(self, table1):
        n1 = index = 0  # n1 - количество несопадающих элементов в двух строках, index- индекс несовпадающего элемента
        table = list()
        for i in range(len(table1) - 1):
            for k in range(i + 1, len(table1)):
                #print(table1[i],"\n", table1[k],"!")
                for j in range(1,len(table1[i])):  # сравнение элементов двух строк
                    if table1[i][j] != table1[k][j]:
                        n1 += 1
                        index = j
                if n1 == 1 :
                    a = table1[i].copy()
                    a[index] = -1
                    a[0] = a[0] | table1[k][0]
                    if a not in table:
                        table.append(a)
                n1 = 0
        return table

    # удаление избыточных строк
    def delete_extra(self, t):
        s = set()
        new_t = t.copy()
        for i in range(len(t)):
            for j in range(len(t)):
                if t[i][0] != t[j][0]:
                    s |= t[i][0] & t[j][0]
            for k in range(len(t)):
                if s in t[k]:
                    new_t.remove(t[k])
            s.clear()
        return new_t

    # вычисляет и возвращает минимальную формулу логической функции.
    def getExpression(self):
        table1 = self.function1()
        for i in range(len(table1)):
            table1[i].insert(0, {i})

        table = table1.copy()
        # минимизация
        while True:
            a = self.minimization(table)
            if not a:
                break
            else:
                table = a.copy()
        table = self.delete_extra(table)
        # вывод
        s = ""
        for i in range(len(table)):
            for j in range(1, len(table[i])):
                if table[i][j] == -1:
                    pass
                elif table[i][j] == 0:
                    s = s + "x" + str(j) + '\''
                elif table[i][j] == 1:
                    s = s + "x" + str(j)
            s = s + ' + '
        return s[:-3]

    # получение значения table.
    def getTable(self):
        pass

    # вывод значения table на экран.
    def printTable(self):
        self.table.display()


t1 = Table(0)
t1.addRow(Row([0, 0, 0, 0], 1))
t1.addRow(Row([0, 0, 0, 1], 1))
t1.addRow(Row([0, 0, 1, 0], 1))
t1.addRow(Row([0, 0, 1, 1], 0))
t1.addRow(Row([0, 1, 0, 0], 1))
t1.addRow(Row([0, 1, 0, 1], 1))
t1.addRow(Row([0, 1, 1, 0], 1))
t1.addRow(Row([0, 1, 1, 1], 0))
t1.addRow(Row([1, 0, 0, 0], 0))
t1.addRow(Row([1, 0, 0, 1], 1))
t1.addRow(Row([1, 0, 1, 0], 0))
t1.addRow(Row([1, 0, 1, 1], 0))
t1.addRow(Row([1, 1, 0, 0], 1))
t1.addRow(Row([1, 1, 0, 1], 1))
t1.addRow(Row([1, 1, 1, 0], 1))
t1.addRow(Row([1, 1, 1, 1], 0))
'''t1.addRow(Row([0, 0, 1], 1))
t1.addRow(Row([1, 0, 1], 1))
t1.addRow(Row([1, 1, 0], 1))
t1.addRow(Row([1, 1, 1], 1))'''
f = LogicFunction(len(t1.rows[0].collection), t1)
f.printTable()
print(f.getExpression())