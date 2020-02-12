# Создайте класс Person, определив для него в конструкторе атрибуты firstname, lastname и age,
# а также метод display(), выводящий информацию об объекте класса на экран.
# Создайте класс Student, унаследованный от Person, определив для него дополнительные атрибуты
# studentID, являющийся уникальным номером для каждого объекта класса, и recordBook,
# содержащий информацию о количестве пятерок, четверок, троек и двоек студента в виде списка.
# В классе Student дополните метод display() выводом значений атрибутов studentID и recordBook на экран.
# Создайте три объекта класса Student для проверки работы методов и выведите информацию о них на экран.


class Person:
    def __init__(self, name, lname, age):
        self.firstname = name
        self.lastname = lname
        self.age = age

    def display(self):
        print("First name: ", self.firstname)
        print("Last name: ", self.lastname)
        print("Age: ", self.age)


class Student (Person):
    id = 0

    def __init__(self, name, lname, age):
        Student.id += 1
        Person.__init__(self, name, lname, age)
        self.studentID = Student.id
        self.recordbook = list()

    def display(self):
        Person.display(self)
        print("Student ID: ", self.studentID)
        print("Record Book: ", self.recordbook)


p1 = Person("Andrew", "Ivanov", 19)
p2 = Person("Ivan", "Smirnov", 17)
p3 = Person("Roman", "Tihonov", 18)
andrew = Student("Andrew", "Ivanov", 19)
andrew.display()
ivan = Student("Ivan", "Smirnov", 17)
ivan.display()
roma = Student("Roman", "Tihonov", 18)
roma.display()


# Создайте класс Professor, унаследованный от Person, определив для него дополнительные
# атрибуты professorID, являющийся уникальным номером для каждого объекта класса, и degree,
# содержащий информацию о научной степени в виде строки. В классе Professor дополните
# метод display() выводом значений атрибутов professorID и degree на экран.
# Создайте три объекта класса Professor для проверки работы методов и выведите информацию
# о них на экран.

class Professor(Person):
    id = 0

    def __init__(self, name, lname, age):
        Person.__init__(self, name, lname, age)
        Professor.id += 1
        self.professorID = Professor.id
        self.degree = str()

    def display(self):
        Person.display(self)
        print("Professor ID: ", self.professorID)
        print("Degree: ", self.degree)


Sam = Professor("Sam", "Kox", 40)
Sam.display()
