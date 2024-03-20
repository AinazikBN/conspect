# #2 
# def list_naob():
#     text = input()
#     text1 = []
#     text1.append(text)
#     a = len(list(text)) // 2 
#     [range (0, a)]
#     text3  = [j for j in range (a, -1)]
#     text.reverse()
#     text1.reverse()
#     text.extend(text1)
#     return text
# print(list_naob())

# def nob(spisok):
#     half = len(spisok) // 2
#     print(' оригинал: ', spisok)
#     spisok[:half] = reversed(spisok[:half])
#     spisok[half:] = reversed(spisok[half:])
#     print(spisok)
# list1 = ['1', '2', ]

#     #3 
# def gen_number():
#     
#     if number.startswith('0888'):
#         for i in number:
#             if i in range (3,9):
#                 return 'PAssword is good'
#             else:
#                 return 'password is false'
            
#     else:
#         return 'write number again'
        

# print(gen_number())
# def gen_number():
#     import random 
#     prefix = '0888'
#     number = prefix +''.join(random.choice('568034') for _ in range (6))
#     return number 
# print(gen_number())


#4
# def add(a,b):
#     return a + b 
# def substract(a,b):
#     return a - b
# def multiple(a,b):
#     return a * b  
# def divide(a,b):
#     return a / b

# print((5,7)) 

#5

# def len_text(a):
#     count = 0
#     letters  = sum([1 for i in a if i.isalpha()])
#     for _ in a:
#         count += 1
#     return count, letters

# print(len_text(input()))



# def print_initials (name, username, middlename):
#     print (username.title())
#     # for i in name:
#     #     print (i.title())
#     print (name[0].upper()'.')
#     # for i in middlename:
#     print (middlename[0].upper()'.')
    

# print_initials('ainazik', 'baltabaeva', 'nurlanbekovna')




