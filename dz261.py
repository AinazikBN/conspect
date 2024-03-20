# month = int(input())
# if month == 12 or 1 or 2:
#     print ("Winter")
# elif month == 3 or 4 or 5:
#     print ("Spring")
# elif month == 6 or 7 or 8:
#     print ('Summer ')
# elif month == 9 or 10 or 11:
#     print ('Autumn')

# num = int(input())
# if 1 <= num <= 20:
#     print('first')
# elif 21 <= num <= 48:
#     print ("Second")
# elif 49 <= num <= 90:
#     print("Third")
# else:
#     print (None)

# num = int(input())
# if num == 1 or 10:
#     print ('Мизинец')
# elif num == 2 or 9:
#     print ('Безимянный')
# elif num == 3 or 8:
#     print ("Средний")
# elif num == 4 or 7:
#     print ('Указательный')
# elif num == 5 or 6:
#     print('большой ')
# else:
#     print (None )


# a = int(input())
# if a % 2 == 0 and a % 4 == 0 and a % 6 == 0:
#     print('Yes')
# else:
#     print ('No')


# ygl1 = int(input())
# ygl2 = int(input()) 
# ygl3 = int(input())
# summa = ygl1 + ygl2 + ygl3 
# if summa == 180 and ygl1 > 0 and ygl2 > 0 and ygl3 >0:
#     print('Yes')
# else:
#     print('No')


# a = int(input())
# b = int(input())
# c = int(input())

# d = b**2 - 4*a*c

# from math import sqrt
# root1 = (-b + sqrt(d)) / (2*a)
# root2 = (-b - sqrt(d)) / (2*a)

# print(root1)
# print(root2)



print ('выберите операцию:')
print ("введите 1 для конвертации фаренгейта в цельсии")
print ('введите 2 для конвертации цельсия в фаренгейт')
choice = int(input('ваш выбор:'))
if choice == 1:
    fareng = int(input())
    c = fareng * 5/9 + 32 
    print(c)
elif choice == 2:
    celsius = int(input())
    f = celsius * 9/5 - 32
    print(f)
else:
    print("Error")




