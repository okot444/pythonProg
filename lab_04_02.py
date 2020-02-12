class Worker:
    'doc class Worker'
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)


class Animal:
    #id = 0
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1
        self.id = Animal.count    

    def display(self):
        #print("Animal id: {} \n Name: {} \n Age: {}".format(Animal.id, self.name, self.age))
        print("Animal id: {} \n Name: {} \n Age: {}".format(self.id, self.name, self.age))


cat = Animal("cat", 3)
hoarse = Animal("hoarse", 10)
otter = Animal("otter", 5)

cat.display()
hoarse.display()
otter.display()

# id - общий член класса , поэтому при выводе он одинаковый у всех объектов

# Измените название атрибута id на count.
# Модифицируйте программу так, чтобы, определив атрибут id, он являлся уникальным для
# каждого объекта, изменяясь на единицу с увеличением количества объектов класса.