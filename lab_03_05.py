'''     Операции cо словарями '''
d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
d5 = d2.copy()  # создание копии словаря
print("Dict d5 copying d2 = ", d5)
# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys())  # список ключей
print("Get dict values d5.values(): ", d5.values())  # список значений print("\n")

# Создайте словарь myInfo, содержащий информацию о Ваших фамилии, имени, отчестве, дне, месяце, годе рождения
# и университете в полях surname, name, middlename, day, month, year, university  соответственно.
# Получите и поочередно выведите на экран списки ключей и значений словаря myInfo. Ознакомьтесь с результатом.

myinfo = dict(surname="котова", name='ольга', middlename="николаевна", day=20,month=2,year=1997, university="itmo")
print("keys : ", myinfo.keys())
print("values: ", myinfo.values())
