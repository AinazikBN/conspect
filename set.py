#=====================Set - Множество==========
# множество - это изменяемый, неупорядочный, итериуемый, неиндексируемый, предназначен для хранения уникальных значений (нельзя хранить изменяемые типы данных), даже нельзя в tuple ([1,2,3])

# set1 = {1,2,3,"hello"}
# print(set1)
# set1 = {1,1,1,1,1,1,1,1}
# print(set1)
# set1 = {1, True, False, 0}
# print(set1)


#=======================Методы множества================
# set2 = {1,2,4,5,8}

#add - добавляет элемент в множество
# set2.add (66)
# print(set2)

#pop - удаляет случайный элемент из set
# popped = set2.pop()
# print(popped)
# print(set2)

#remove -  удаляет элемент из  set по значению, если не найдет значение если не найдет означение выходит KeyError
# set2.remove(2)
# print(set2)

#difference -  находит различия между множеством и другой коллекцией (множество)
set1 = {1,2,3}
set3 = {3,4,5}
print(set1.difference(set3)) #1,2
print(set3.difference(set1)) #4,5 

#symmetric_difference - находит только разные значения в множества
print(set1.symmetric_difference(set3)) # 1,2,4,5

# intersection - выводит одинаковые значения коллекции 
print(set1.intersection(set3)) #1

sdvig = int(input())
string_ = input()