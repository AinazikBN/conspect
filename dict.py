#===================Dict - Словарь==================
# dict - это изменяемый, итерируемый, неупорядочный, неиндексируемый тип данных, хранит в парах (ключ: значение) (key:values)

# user = {"name": "Anton", "login": 'adams', 'password': 12345}
# print(user["login"]) #adams
# print(user)

# ключами в словаре могут быть только неизменяемые типы данных 
#ключи должны быть уникальными, не должны повторяться , если же они повторяются то сохраниться последний

# значение могут быть любые типы данных и они могут повторяться 

# dict_= {1: 'a', 2: 'b', 3: 'c'}
# dict_[4] #KeyError 

# #==================Создание================
# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# dict_ = dict([(1, 'a'), (2, 'b'), (3, 'c')])

# dict_ = {1: {1: 'a', 2: 'b'}, 2: 'c'}

# dict_['name']='Ertay'
# dict_['login']='xyq'

# print(dict_)



#================Методы словарей=====================
# get - сетод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение

user = {"name": "Anton", "login": 'adams', 'password': 12345}
# print(user['email'])
# print(user.get('email', "Такого ключа нет"))

# pop - метод, удаляет пару по ключу и возвращает значение 
# remove_elem = user.pop('password')
# print(remove_elem)
# print(user)


# popitem - метод который удаляет последнюю пару и возвращает ее 
# remove_item = user.popitem()
# print(remove_item)
# print(user)

#update - метод который расширяет словарь парами из другого словаря 
# dict1 = {1: 'a', 2 : "b"}
# dict2 = {3: 'c'}

# dict1.update(dict2)
# print(dict1, dict2)

# #clear - очищает словрь 

# dict1.clear()
# print(dict1)


# fromkeys - метод который создает новый словарь используя список ключей
# dict1 = dict.fromkeys(["Anton", 'Alina', "Adina", 'Adilet'], 'name')
# print(dict1)

# keys, values, items
# keys - метод, который возвращает ключи 
# values - метод который возврщает значение
# items - метод который возврщает tuple (ключ, значение )

# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())


# ====================Итерирование словарей ==================

user = {"name": "Anton", "login": 'adams', 'password': 12345}
# for key in user.keys():
#     print(key)

new_user = {}
for key, values in user.items():
    new_user[values] = key
print(new_user) 

# university = {"ITs": 124, "economy": 67, "medicine": 54}
# university['IT'] = 100
# university1 = {"lingvist": 15}
# university.update(university1)
# university.pop("medicine")
# print(sum(university.values()))
# print(university)

# for value in university.values():
#     value += int(value)
# print(value) неправильно 



n = int(input())
spisok = []
spisok1 = {}
for i in range (n):
    st = input()
    spisok.extend(st)
for i in range (n):
    spisok1[i + 1] = st 

print(spisok1) 


