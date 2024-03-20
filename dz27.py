#=================Homework 
#1 
# str1 = (input())
# str2 = (input())
# print(str1.upper())
# print(str2.lower())


#2
# bool1 = bool(1)
# print(type(str(bool1)))




#3
# name = input(("Введите ваше имя: "))
# age = input("Введите ваш возраст: ")
# movie = input("Введите ваш любимый фильм: ")
# print (f"Привет {name}\nВаш фильм очень интересный {movie}")


#4
# simvol = input('Введите символ:')
# text = """Этот документ описывает соглашение о том, как писать код для языка python, включая стандартную библиотеку, входящую в состав python.
# PEP 8 создан на основе рекомендаций Гуидо ван Россума с добавлениями от Барри. Если где-то возникал конфликт, мы выбирали стиль Гуидо.
# И, конечно, этот PEP может быть неполным (фактически, он, наверное, никогда не будет закончен)."""
# print(text.split(simvol))


# #5
# count = 0
# text = """Ключевая идея Гуидо такова: код читается намного больше раз, чем пишется. Собственно, рекомендации о стиле написания кода направлены на то, чтобы улучшить читаемость кода и сделать его согласованным
# между большим числом проектов. В идеале, весь код будет написан в едином стиле, и любой сможет легко его прочесть."""
# for a in text.split():
#     if a.isalpha() and len(a)>1:
#         count = count + 1
#     elif a[: -2].isalpha:
#         print(a[:-2])
#         count = count + 1
# print(count)

#6 
# text = """
# Пробелы - самый предпочтительный метод отступов.
# Табуляция должна использоваться только для поддержки кода, написанного с отступами с помощью табуляции.
# Python 3 запрещает смешивание табуляции и пробелов в отступах.
# Python 2 пытается преобразовать табуляцию в пробелы.
# """
# print (len(text))


#7 
# a = """Пробелы - самый предпочтительный метод отступов.
# Табуляция должна использоваться только для поддержки кода, написанного с отступами с помощью табуляции.
# Python 3 запрещает смешивание табуляции и пробелов в отступах.
# Python 2 пытается преобразовать табуляцию в пробелы."""
# print('|'.join(a))


# text = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."
# print (text.split('|'))

#8
# text = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."
# print(text.title())

#9
# text = (input())
# text1 = text.upper 
# print (text1)


#10
# text = "Dj(.=(.(,,,,,ango i,,s a hi,,,,gh-,.,.,.,.level Python( web framewor(.....k"
# print(text.replace('.,(=', " "))

#11
# text = input()
# if text.isdigit:
#     print("ВВести ")
# else:
#     print(str(text.lower()))

#12
# num = (input())
# if num.isdigit():
#     print(int(num*2)**3)
# elif num.isalnum():
#     print('нельзя')




# count = 0
# srt = input().lower
# for a in srt:
#     if a == "a" or a == 'e' or a == 'u' or a == 'o' or a == 'i' or a == "y" :
#         count = count + 1 
# print (f"В вашей строке насчитано {count} гласных букв")


# name = input()
# znak = int(len(name)/2) + 1
# user = name.swapcase() 
# password = user [:znak] + "&" + user [znak:] + "$"

# print(f'Ваш сгенерирован пароль: {password}')



# word = input().lower()
# if word == word[::-1]:
#     print('это палиндром')
# else:
#     print ('это не палндром')























