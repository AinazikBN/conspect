#====================List==================
#List (список) - изменяемый, индексируемый, упорядоченный, итерируемый тип данный предназначенный для хранения любых данных в определенном порядке.

list1 = [1,2,3,4,"hello", [2,3,4,5], None, True]
# list1[4] #hello
# print(list1[5][3])

list2 = list('ada')
print(list2)

# list3 = (range(1,11)) 
# print(list3)
# #range - генератор какго-нибудь диапазона range 

# list_sum = list2 + list3
# print(list_sum)

# list4 = [4] * 5 ##[4,4,4,4,4]

# #=================Методы==============
# print(dir(list))

# #append - добавляет элемент в конец списка
# list5 = []
# list5.append(4)
# list5.append ('ada')
# list5.append ({2,2,2,23,5,5,6,7})
# print(list5)


# #pop - удаляет элемент из списка по индексу и возвращает этот удаленный элемент, если не указать индекс то он удалит последний элемент
# list6 = [1,2,3,4,5,6, "ada", "ada"]
# list6.pop(1)
# list6.pop()

# #remove - удаляет жлемент из списка по значению
# list6.remove(1)
# list6.remove("ada")


# #count - считает количечство принятого элемента в списке 
# print(list6.count("ada"))


# #index - возвращает индекс первого вхождения принятого эдемента 
# print(list6.index("ada"))
# ada = list6.index('ada')
# list.pop(ada)
# print(list6)

#insert - добавялет эдемент в список по индексу
list2 = [1,2,4,5,6]
list2.insert(2,3)
print(list2)


# extand -  расширяет список засчет другого списка
# list1 = [0,0,0]
# list2 = [1,1,1]
# list1.extend(list2)
# print(list1)



# # reverse - изменяет списокб расставляя его элементы в обратном порядке 
list_1 = [6,5,4,3,2,1]
list_1.reverse()

# # sort - сортирует  спсиокб состояющий из элементов одного типа данных
# list_1.sort()
# print(list_1)

# #sort (key = функция с логикой сортировки, reverse = True либо False)
# print(list_1.sort(reverse=True))

#clear - очищение списка
# list_1.clear()
# print(list_1)



# a,b,c,d = [[1,2,3,4],2,3,4] #множественное присвоение 
# print(a,b,c,d)

# list1 = list('he l o wo r ld')
# # list2 ="".join(list1) #склеивание списка в строку
# print(*list1) #распаковка списка
# print(list2)


# hello = list1
# list1.pop()
# print(list)
#copy - метод копирования данных внутри списка
# hello = list1.copy()
# list1.pop()
# list1.append('123445')
# print(hello)
# print(list1)



#===============Операторы принадлежности=======
# numbers = [2,3,6,8,10]
# if 2 in numbers:
#     print("number 2")
# else:
#     print('number 2 is epcent')


# #================Max() Min() Sum()==============
# numbers = [12,3445,56,56,5]
# print(sum(numbers)) #summa
# print(min(numbers)) #наименьшее число
# print(max(numbers)) #наибольшее число
 
# numbers[1] = 13
# print(numbers )


# #==================Кортеж=========
# tuple_ = (1,2,3)
# print(type(tuple_))


# a = [(1,),(2,),(3,),()]



# names = ["Миша", "B",'c','d','e']
# strok = ' '
# print(strok.join(names))
 

