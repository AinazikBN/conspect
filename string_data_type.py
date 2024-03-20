#                           String (строки)
# строки - неизменяемый тип данныхб который предназначен для хранения текста (последовательностс одинарными кавычкамии символов)б заключенного в одинарные или двойные кавычки 
striing = 'строка с одинарными кавычками '
striing2 = "строка с одинарными кавычками"

stringg = "Don't "

stringg2 = 'Petter is "strong" man'
print(stringg2)

string3 = 'Petter isn\'t "strong" man' #обратный слэш подсказывает питону что после него идет символ кавычки



#========================Экранизация строк============
"\n" # перенос на новую строку
string4 = 'Ada course \nThe better course'
print(string4)

"\t" #табуляция
print("hello\tworld")
'\'' # отображение кавычки
"\"" # отображение двойных кавычек
'\\' # отображениее одного слэша
'\v' #перенос строки на новую со смещением вправо на длину предыдущей строки 
print ('hello\vworld\vada\vcourses')
'\r' # перенос каретки на начало строки
print ('Hello world\rHo')



string5 = """
Многострочный текст 
в одинарных кавычках,
тут можно ставить 'любые' кавычки
"""



"=================Форматирование строк================="
title = 'iphone 13'
price = 900
format1 = f"Название: {title}\nцена: {price}"
print (format1)

format2 = 'Название: {}\nЦена: {}'
print (format2.format('хлеб', 15))
print (format2.format(title, price))

format3 = 'Название:%s  \nЦена: %s'
print (format2.format('хлеб', 15))
print (format2.format(title, price))






string6 = "hello" + "" + "world" # конкатенция
print (string6)
string7 = string6 * 5 
print(string7)





"=====================ИНдекс====================="
# индекс - порядковый номер элемента в последовательности (символ строке) начинается с 0 1 2 3

"""
h e l l o w o r l d
0 1 2 3 4 5 6 7 8 9
-9               -1
"""

string = "hello world"
print (string [-2])


#срез - это опредленная часть строки
#string [start, end, step] 
print (string [0: 5])
print (string[-5:])
print (string [::-1]) #переворичваем слово
print (string[::2])



"====================Методы строк======================"

# Методы - это функции к которым относятся к опредленному классу (типу данных), к ним обращаются через точку 

print(dir(str)) # посмотреть все методы string

string10 = "hello"
print (string.upper()) # все большие буквы 
upper_string = string10.upper()
print(string10, upper_string) 

print(string10.lower()) # все маленькие буквы 

print(string10.swapcase()) # меняет регистр всех букв 

print(string.title()) #каждое слово будет с большой буквы

print(string10.capitalize()) #делает первую букву большой а остальные маленькими 

print(string10.count('L')) #считает символы 

print(string10.startswith('hel')) #проверка начинается ли строка с заданных символов

print(string10.endswith('ld')) # проверка заканчивается ли строка с заданных символов

print(string10.isupper()) # проверка всех символов на верхниый регистр  True False

print(string10.islower()) #  nроверка всех символов на нижний регистр  True False

print(string10.isdigit ()) #проверка явялется ли строка числовой 

print(string10.isalpha ()) #проверка явялется ли строка буквами 

print(string10.isalnum ()) #проверка явялется ли строка буквами и числами или все вместе

print(string10.split('*')) #разделитель

print("&".join(['world', string10])) #склеивает все 

print("           hello        world         ".strip()) #убирает с начала и конца 
print("           hello        world         ".strip()) #убирает с начала 
print("           hello        world         ".strip()) #убирает с конца

print(string10.replace('hello', ' привет')) # меняет символ на указанный 


