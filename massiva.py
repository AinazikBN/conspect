# n = 3
# m = 2
# array = []
# i = 0
# while i < n:
#     array.append([])
#     j = 0
#     while j < m:
#         array[i].append(0)
#         j += 1
#     i += 1
# print(array)

# n = 3
# m = 2
# array = []
# for i in range(n):
#     array.append([])
#     for j in range(m):
#         array[i].append(0)
# print(array)

# n = 3
# m = 5
# array = list(range(n))

# for i in range(n):
#     array[i] = list(range(m))

# print(array)

# array = [[1,2,3],
#           [4,5,6], 
#           [7,8,9]]
# n = len(array)
# m = len(array[0])
# i = 0
# while i < n:
#     j = 0
#     while j < m:
#         print(array[i],[j], end = ' ')
#         j += 1 
#     print()
#     i += 1

# for i in range (n):
#     for j in range(m):
#         print(array[i][j], end=' ')
#     print()


# n = 3
# m = 3
# array = list(range(n))
# for i in range(n):
#     array[i] = list(range(m))
#     for j in range(m):
# #         text = f'Введите эдмент в  {i}*{j} позицию'
# #         el = input(text)
#         array[i][j]
# print(array)


"=======================Comperhensions=============="
#Генератор - с помощью которого мы можем создать последовательность тспользуя цикл for в одну строку
# Результат for элемент in последовательность
# Результат for элемент in последовательность 
# Результат for элемент in последовательность if фильтр 
# Результат if условие else тело for элемент in последовательность if фильтр 
# 

# comphrhensions = (i for i in range (1,6))
# print(*comphrhensions)

# Генератор - это итеруемый обьект, который не хранит в себе полностью всю последовательность, а создает их когда требуется 
# print(next(comphrhensions))
# print(next(comphrhensions))
# print(next(comphrhensions))
# print(next(comphrhensions))
# print(next(comphrhensions))
# print(next(comphrhensions)) #StopInteration 
# next - функция, которая запрашивает у генератора текущий элемент и генератор создает следущий элемент 

"======================Синтаксический сахар================="
# list comperhension 
# list_comp = list(i ** 2 for i in range (1,6))
# list_comp = [i ** 2 for i in range (1,6)]
# # print(list_comp)

# list1 = []
# for i in range (1,6):
#     list1.append(i**2)
# print(list1)

# newlist = [1, 'Hello', 2, True, 2, 2, False, 'string']
# new = [i for i in newlist if type(i)==str]
# print(new)

"================Dict comperhension=========="
# dict1 = dict((i, i ** 2)for i in range (10))
# dict1 = {i: i ** 2 for i in range (10)}
# print(dict1)

# dict2 = {'a': [1,2,3,4,11], 'b': [1,2,3], 'c': [2,3,4,5]}
# new = {key: sum(value) for key, value in dict2.items()}
# print(new)

example = {i:['hello world' for i in range (5)] for i in range (3)}
print(example)

#==============Set comperhension=================
# set1 = {1,2,3,4,5,1}
# set2 = {i for i in set1}
# print(set2)


#===================Вложенные comperhension===========
# dict1 = {v: [i for i in range (1, v+1)] for v in range (1,6)}
# print(dict1)

# dict1 = {k: list(range(1, k + 1)) for k in range (1,6)}
# print(dict1)

# dict1 = {k: {v: [l for l in range (1, v+1)] for v in range (1, k+1)} for k in range (1,6)}
# print(dict1)


#=======================RAndom=============
import random 

a = random.randint(0,10)
print(a)



# again = "д"
# while again.lower() == "д":
#     print('Бросаем кубики..')
#     print("Значение граней: ")
#     print(random.randit(1,6))
#     print(random.randit)