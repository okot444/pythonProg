import time

class Ticket:

    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket:", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print("createDate: ", time.asctime(self.createDate))
        print("owner: ", self.owner)
        print("deadline: ", time.asctime(self.deadline))


# создание объект класса

ticket1 = Ticket(time.localtime(), "Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))

# вызов метода
ticket1.display()

# получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))

# проверка наличия атрибута
print("hasattr: ", hasattr(ticket1, "owner"))
setattr(ticket1, "owner", "Alexei Petrov")  # установка значения атрибута
print("Owner(setattr): ", ticket1.owner)

# Раскомментируйте строки: Объясните поведение программы.
# Исправьте программу с помощью стандартных функций так, чтобы ошибка не возникала.
delattr(ticket1, "owner")  # удаление значения атрибута

setattr(ticket1, "owner", "Petr Smirnov")
print("delattr: ", ticket1.owner)
# если аттрибут удален, нельзя получить доступ к этому члену класса ("owner")


# Раскомментируйте строкию. Объясните поведение программы.
del ticket1  # удаление объекта
# print(ticket1)
# объект удален, нельзя получить доступ к объекту

# Получите текущее время сервера (или компьютера) и выведите его на экран в аналогичном формате:
# Thu Mar 9 2017 14:53:55.

print (time.asctime())

# Создайте объект типа time по следующей строке с использованием соответствующей
# функции библиотеки time: 17.07.2017 10:53:00.
time.strptime("17.07.2017 10:53:00 ", "%d.%m.%Y %H:%M:%S ")

# time.strptime("17.07.2017 10:53:00", "%d.%m.%Y %H:%M:%S")
#from datetime import time
#mytime = datetime.strptime("17.07.2017 10:53:00", "%d.%m.%Y %H:%M%S")
#mytime = time.time()
#print (type(mytime))
