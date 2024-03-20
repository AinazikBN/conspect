#=================Домашка==================
#1 
# num1 = int(input('Put your first number: '))
# num2 = int(input('Put your second number: '))
# yourall = int(input("Write your answer: "))
# compall = num1 * num2 
# if compall == yourall:
#     print ("Right!", compall)
# else:
#     print ('Wrong,', "Right answer is", compall, )

#2
# season = (input("Write number: "))

# if season == 3 or season == 4 or season == 5:
#     print("Птицы пели прекрасные песни")
# elif season == '6' or '7' or '8':
#     print("Солнце светило ярче чем когда-либо")
# elif season == '9' or '10' or '11':
#     print ("Урожый был невероятным")
# elif season == '1' or '2' or '12':
#     print("за окном падал белый снег")
# else:
#     print('Такого месяца не существует') 

month = int(input())
if 1 <= month <= 2 or month == 12:
    season = 'за окном падал белый снег'
elif 3 <= month <= 5:
    season = 'Птицы пели прекрасные песни'
print (season)

#3 
a = int(input())
if 0 < a < 5:
    print( "Верно")
else:
    print('Неверно') 


#28
a = int(input())
b = int(input())
c = int(input())


