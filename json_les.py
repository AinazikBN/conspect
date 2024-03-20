'===========================Json=========================='
#JavaScript Object Nonation - универсальный формат, в котором мы можем хранить данные в типах данных, понятный для всех языков прогромирования


# Десериализация - перевод с json строки в python обьект 
# loads - метод для десериалиция с json строки 
# load - метод для десерализация с json файла


# Сериализация - перевод с python в json строку 
# dumps - метод для сериализация в json строку
# dump - метод для серилизация в json файл 
import json

# with open ('test_js.json', 'w') as file:
#     json.dump({'anton': 12, 'adilet': 11}, file)

# with open('test_js.json') as file:
#     content = json.load(file)

import json

def read_(id = None):
    with open('db.json') as file:
        f = json.load(file)
        if id == None:
            print(f)
        else:
            for i in f:
                if i['id'] == id:
                    print(i)

def create_(id,title,description,price):
    with open('db.json') as file:
        f = json.load(file)
    with open('db.json', 'w+') as file:
        f.append({'id': id, 'title': title, 'description': description, 'price': price})
        json.dump(f, file)

create_(1,'iphone13', 'smartphone', 1000)
create_(2,'iphone15', 'smartphone', 1500)

read_(1)
read_()
 

def delete_(id):
    with open('db.json') as file:
        f = json.load(file)
        for num, slovar in enumerate(f):
            if slovar ['id'] == id:
                f.pop(num)
        with open('db.json', 'w+') as file:
            json.dump(f, file) 
delete_(2)


def update_(id, chose, move):
    with open('db.json') as file:
        f = json.load(file)
        with open('db.json', 'w+') as file:
            for elem in f:
                if id == elem['id']:
                    elem[chose] = move
                json.dump(f, file)

# update_(2,'price', 1399)
# read_(2)
# update_(2,'description', 'ultra new')
# read_(2)