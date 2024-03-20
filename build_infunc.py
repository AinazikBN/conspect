'============================Встроенные функции======================='
#map, filter, reduce, zip, enumerate, all, any

#zip - соединяет несколько последовательностей (получая генератор в котором элемент tuple) 
# list1 = [1,2,3,4,5,6]
# list2 = ['a','b','c']
# list3 = [1.2]
# zipped = zip(list1,list2,list3)
# print(*zipped)
# print(list(zipped))


names = ['Alina', 'Anton', 'Mark']
ages = [14,16,17]
people = dict(zip(names, ages))
print(people)
for name, ages in zip(names,ages):
    print(name,ages)

# enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)
# enumerated = enumerate('hello')
# print(next(enumerated))

# names = ['Ada', 'Bob', "Max"]
# enum  = list(enumerate(names, start = 1))
# print(enum)

#map - функция высшего порядка, принимает другую функцию и итерируемый обьект, выполняет заданную функцию на каждый элемент последовательности 

# def x10 (num):
#     return num * 10

# print(x10)

# nums = [1,2,3,4,5]
# n = list(map(lambda x: x*10 , nums))
# print(n)

# text = list(map(int, input("Put your number: ").split()))
# print(sum(text), ' summa')

# num = [1,2,3]
# num2 = [4,5,9]
# num3 = [6,7,8]
# sums = list(map(lambda n1, n2, n3: n1 + n2+ n3, num, num2, num3))
# print(sums)


# filter - функция высшего порядка, возвращающая генератор, с элементами прошедшими фильтр (какое-то условие), принимает функции и последовательность (func, iterable)

# people = [
#     ("John", 22),
#     ("Adrian", 14),
#     ("Adam", 12),
#     ("Mark", 18)
# ]
# # def is_adult(person):
# #     return person[1] >= 18
# print(list(filter(lambda p: p[1]>= 18, people)))


# list_ = [3,-5,0,10,-3]
# filtered = list(filter(lambda i: i >0, list_))
# print(filtered)


#reduce - функция высшего порядка которая принимает другую функцию и последовательнсоть, возврщает один элемент
# from functools import reduce

# list_ = [1,2,3,4,5]
# print(reduce(lambda x,y: x + y, list_))

# string = 'hello'
# print(reduce(lambda x,y: x + '!' + y, string))

# users = [
#     {'name': 'anton', 'age': 20},
#     {'name': 'anna', 'age': 12},
#     {'name': 'aza', 'age': 50},
#     {'name': 'beka', 'age': 3}
#     ]
# print(reduce(lambda x, y: x if ['age']>y['age'] else y, users)['name'])

#all - функция которая принимает итерабельный обьект и возвращает True иначе False 
# print(all([True, 1, {}]))
# print(all([True, 1, '']))

# #any - функция которая принимает последовательсноть и возвращает True если хотя бы один элемент был истинный (True) иначе False
# print(any([False, False, False]))
# print(any([1, False, False]))


