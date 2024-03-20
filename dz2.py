#1 
# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print (d1["b"] == d2["b"])

#2 
# person = {"name": "Kelly", "age":25, "city": "New york"}
# print(person['age'])

#3 
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# list1 = sample_list[0]
# list2 = sample_list[1]
# list3 = sample_list[2]
# sample_set.add(list1)
# sample_set.add(list2)
# sample_set.add(list3)
# print(sample_set)

# for i in sample_set:

#4 
# set1 = {6, 4, 2, 5, 7, 8, 10, 9}
# set1.remove(7)
# print(set1)

#5
# set1 = {'Python', 'it', 'c++', 'java', 'programming'}
# set2 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set1.intersection(set2))

#6 
# set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# set2 = {'Python', 'it', 'c++', 'java', 'programming'}
# print(set3.difference(set2))

#7
# set1 = {'Python', 'it', 'c++', 'java', 'programming'}
# set1.add('JS')
# set1.pop()
# print(set1)

#8
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu['besh_barmak'] = 135
# menu['lagman'] = 135
# menu.pop('borsh')
# print(menu)

#9
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu1 = dict.fromkeys(['Coca-Cola', 'Sprite', 'Fanta'], 'drinks')
# menu2 = menu1
# # menu.update(menu1)
# # print(menu)
# drinks = {}
# for key, values in menu2.items():
#     drinks[values] = key
# menu.update(drinks)
# print(menu)
 
#10
# set1 = {"add", 'pop', 'remove', 'symmetric_difference', 'difference', 'intersection ' }
# dict1 = {'get', 'pop', 'popitem', 'clear', 'update', 'fromkeys'}
set1 = set(dir(set))
# set2 = set(dir(dict))
# set1.intersection(set2)
# for i in set1.intersection(set2):
#     if str(i).startwith("__"):
#         continue
#     print(i)

#11
# set1 = []
# for i in range (0,10):
#     i = int(input())
#     set1.append(i)
# set2 = fronzenset(set1)
# print(set

#12 
# suitcase = []
# for i in range (5):
#     i = input()
#     suitcase.append(i)
# suitcase.pop(4)
# print(suitcase)

#13
# ferma1 = {'корова', 'курица', 'овца', 'заяц'}
# ferma2 = {'корова', 'козел', 'собака', 'заяц'}
# ferma3 = ferma1.intersection(ferma2)
# print(ferma3)

#14
# ferma1 = {'корова', 'курица', 'овца', 'заяц'}
# ferma2 = {'корова', 'козел', 'собака', 'заяц'}
# print(ferma2.difference(ferma1))

#15
# stroka = input()
# list1 = []
# for i in stroka:
#     list1.append(i)
# li = set(list1)
# print(li)
# print(len(li))

# list_ = input().lower().split()
# print(list_)
# for i in list_:
#     print(len(set(i)))