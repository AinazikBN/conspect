#================Функция=====================
# Функция - это именнованный блок кода, который может принимать аргументы и возвращать резльтат и которая назвается множество раз в других частях программы
#Они создается благодаря ключевому слову def 
# При наименовании функции нужно использовать стиль snake_case

#парметры функции - это переменные которые будут принимать ваша функция для того чтобы вы смогли работать с данными которые попадают в вашу функцию 
#аргумент - данные которые мы пердаем для парметров при вывозе функции
#return (по умолчанию возврщает None) - оператор который нужен чтобы функция возвращала результат 



# def name_of_function(a,b параметры сколько угодно):
#     <body> код, который имеет некую логику 
#     return оператор, который возвращает результат выполнения функции 


# def print_our():
#     print('*'*120)
#     return ('hello ada')


# print('hello word')

# print_our()
# print(print_our)

# car = None
# if car is  None:
#     print('Машина есть')

# def sum_our():
#     number1 = int(input())
#     number2 = int(input())
#     return f'{number1} + {number2} = {number1 + number2}'

# print(sum_our())


# def say_hello_world():
#     name = input()
#     return f'{name} говорит hello world'

# print(say_hello_world())

# def summa_n():
#     n = int(input())
#     for i in range (1, n+1):
#         s = sum([i for i in range (1,n+1)])
#     return f'Я знаю что сумма чисел от 1 до {n} равна {s} где в качестве {n} и {s} вам необходимо подставить значения'

# print(summa_n())

# def exponention():
#     n = int(input())
#     return (n** 2, n ** 3)
# print(exponention())


# def sum_num():
    # stroka = input()
    # # if stroka.isdigit():
    # s = sum([int(i) for i in stroka.isdigit()])
    # return s
    
# print(sum_num())

# def sum_num():
#     stroka = input()
#     s = sum([int(n) for n in stroka if n.isdigit()])
#     return s
# print(sum_num())


# def check_password():
#     s = input()
#     num = sum([1 for n in s if n.isdigit()])
#     let = sum([1 for upper in s if upper.isupper() ])
#     c = sum([1 for sym in s if sym in "!@#$%^*"])
#     len_our = len(s) >= 10
#     if num>=3 and let >= 1 and c >=1 and len_our:
#         print('Perfect')
#     else:
#         print("easy")

# check_password()


# string_ = '1234abs'
# def our_len(str1):
#     count = 0 
    # for _ in str1:
    #     count += 1
    # return count
# print(our_len(string_))


#====================Виды параметров=================
#Обязательные 
#Необязательные:
    #  с дефолтом (со значению по умолчанию)
    # args (ввсе позиционные агрументы, которые не попали в обязательные и с дефолтом)
    # kwargs (все лтшние именованные параметры)
# def greet(*args):
#     for name in args:
#         print(f'Привет {name}')

# def my_greet(**kwards):
#     name = kwards.get('name')
#     print(f' Hello{name}')
# my_greet(age = 12, name = 'ada')
#                   Виды аргументов 
# 1. Позиционные (по позиции)
# 2. Именованные (по названию (параметр = значения)) 

# def add_10(num1, num2 =10):
#     """  Складывает два числа"""
#     return num1 + num2 
# print(add_10(5))
# print(add_10(1,2))
# print(add_10(num1=2,num2=2))

#python Turor - читает питон по строкам 
"""
чем хороши функции?
1 Помогает избегать повторений одинаковых фрагментов кода
Функции соблюдают принцип DRY (dont repeat yourself)
2 Упрощают внесение измений в повторяемых блоках кода 
3 Позволяет разбить задачи на подзадачи 
"""
# =======================Lambda======================              
# lambda - анонимная функция, которая записывается в одну строку 
# lambda_fund = lambda x: x**3
# print(lambda_fund(5))

# calc = {
#     '+': lambda n1, n2: n1 + n2,
#     '-': lambda n1, n2: n1 - n2,
#     '*': lambda n1, n2: n1 * n2,
#     '/' : lambda n1, n2: n1 / n2,
#     '//' : lambda n1, n2: n1 // n2,
#     '%' : lambda n1, n2: n1 % n2
# }
# def main():
    # num1 = int(input("number1: "))
    # num2 = int(input("number2: "))
    # operator = input('operator: ')
    # func_ = calc [operator]
    # res = func_(num1,num2)
    # return res
# print(main())





#======================Register, Login=================

database = [
    {'name': 'user1', 'password': (12345)},
    {'name': 'user2', 'password': (12346)},
    {'name': 'user3', 'password': (12347)},
    {'name': 'user4', 'password': (12348)}
]

def in_database(name):
    for user in database:
        if user['name'] == name:
            return True
        else:
            return False
print(in_database('user1'))


def register_database(name, password1, password2):
    if in_database(name):
        return "user has already been"
        return None
    if password1 != password2:
        return "Порали не совпали"
    user = {'name': name, "password": password1}
    database.append(user)
    return 'Вы успешно зарегистровались'
print(register_database('Ainazik', 123423, 123423))

# print(database)

def login_database(name,password):
    if not in_database(name):
        return "Пользователь не найден "
    for user in database:
        if user['name'] == name:
            if user['password'] != password:
                return 'Пароль не верный'

    return "Вы успешно зашли"    
# print(register_database('Anton', 222, 222))
# print(login_database("Anton", 222))


# def main():
#     print('Добро пожаловать')
#     while True:
#         action = input('Введите что то из этого --> regidter: 1, login: 2, exit: 3  ')
#         if action == "3":
#             break
#         elif action == '1':
#             name = input('введите имя пользователя: ')
#             password1 = input("введите пароль: ")
#             password2 = input("введите пароль снова: ")
#             print(register_database(name, password1, password2 ))
#         elif action == '2':
#             name = input('введите имя пользователя:')
#             password1 = input("введите пароль:")
#             print(login_database(name, password1))
#         else:
#             print('Не корректный выбор')
# main()

# text = input()
# letter = input()
# def count_letter(text,letter):
#     # text = input()
#     # letter = input()
#     # for i in text:
#     #     if i is letter:
#     print(text.count(letter))
#         # else:
#         #     print("Нету такой буквы: ")
# count_letter(text, letter)