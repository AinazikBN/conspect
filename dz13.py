#1
# def step(a,b):
#     stepen = 0
#     try:
#         stepen = a ** b
#     except TypeError:
#         stepen = int(a) ** int(b)
#         print(stepen)

# step(3,'2')

#2 
# with open('letters.py', 'w') as file:
#     a = input()
#     file.write(a)   
#     try:
#         b = (int(i) for i in a )
#         print(*b)
#     except:
#         print('строка содержит несоотвестующие числа')

#3
# try:  
#     with open( 'letters.py', 'r') as file:
#         f = file.read()
#         if 'w' in f:
#             print('в тексте есть буква w')
#         else:
#             print('в тексте нет буква w')
# except FileNotFoundError:
#     print("Введите существующий файл")

#4
# try:
#     name = input()
#     country = input()
#     birth = int(input())
#     with open ('data.txt', 'w') as file:
#         # file.write (name + '\n')
#         # file.write(country + '\n')
#         # file.write(birth + '\n')
#         file.write(f'Name: {name}\nCountry: {country}\nBirthday:{birth}')
#         print('ok')
        
#except ValueError as e:
#     print('Error:', e)

#5 
# def name_age(*args, **kwards):
#     try:
#         name = kwards.get('name')
#         age = kwards.get('age')
#         print( name, age)      
#     except KeyError:
#         print('error')
# name_age(name='asd', age = 12)
# name_age(name='asd')


#7
# l1 = [2, 3, 0, 1]
# l2 = [10, 20, 30, 40]
# result = []
# try:
#     for i in l1:
#         i == 0 
#         print(l2[i])





#6
# def add(a,b):
#     try:
#         print(a + b)
#     except:
#         print('Введите числа')
    
# def minus(a,b):
#     try:
#         print(a - b)
#     except:
#         print('Введите числа')
# def mult(a,b):
#     try:
#         print(a * b)
#     except:
#         print('Введите числа')
# def delen(a,b):
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print('на ноль делить нельзя')
#     except ValueError:
#         print('Введите числа')

# add(0,0)
# minus(2,4)
# delen(3,0)
# mult(12,7)



