#1 
# def num_bers():
#     list_data = {int(value) for value in input().split()}
#     set1 = min((list_data))
#     return set1 
# print(num_bers())


#2 
# def kredit_schet():
#     kredit = int(input())
#     if kredit > 100_000:
#         procent = 7.89
#         pereplata = round(kredit * (procent / 100),2)
#         print(pereplata)
#     else:
#         print("Введите число больше 100000")

# kredit_schet()

#3
# def num_split():
#     stroka = input()
#     n = ''.join([i for i in stroka if i.isdigit()])
#     if n:
#         integer = int(n)
#         print( integer)
#     else:
#         print("цифр нет ")

        
# num_split()

#4
# month = int(input("month: "))
# year = int(input('year: '))
# def schet_days():
#     # month = int(input())
#     # year = int(input())
#     days_in_month = 30 * month
#     days_in_year = 365 * year 
#     summ = days_in_month + days_in_year
#     return summ
# print(schet_days())


#5
# def dict_num():    
#     example = {i: int(i)**3 for i in range (1,11)}
#     return example 
# print(dict_num())




#6
# def summa_num():
#     # summ = 0 
#     # for i in range (1, 51):
#     #     summ += i 
#     summ = sum(range (1,51))
#     return summ
# print(summa_num())