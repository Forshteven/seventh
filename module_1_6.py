my_dict = {"Sergey":1992, "Vlad":1998} #создать переменную и присвоить ей словарь
print(my_dict) #вывести на экран словарь
print(my_dict.get("Sergey")) #вывести на экран одно значение по существующему ключу
print(my_dict.get("Nikolay")) #вывести на экран одно значение по отсутствующему ключу
my_dict.update({"Vasily":1995,
                "Artem":1994})#добавить две произвольные пары в словарь
print(my_dict.pop("Artem"))#удалить одну из пар в словаре по существующему ключу и вывести её значение на экран
print(my_dict) #вывести на экран словарь


my_set = {122, 144, 225, 144, "блинчики", False, 169, 225, 122} #создать множество с разными типами данных и повторяющимися значениями
print(my_set) #вывести на экран множество
my_set.update([8, 15]) #добавить два произвольных элемента, которых ещё нет
my_set.remove(122) #удалить один произвольный элемент из множества
print(my_set) #вывести на экран изменённое множество