#1
# n = 3
# m = 4
# array = list(range(n))
# for i in range(n):
#     array[i] = list(range(m))
#     for j in range(m):
#         array[i][j]
        
# print( array, end=' ')
# matrix = [[1 for j in range (3)]for i in range (3)]
# print(matrix)
# #2
# matrix = [[i + j * 3 +1 for j in range]]



#3
# a = 3 
# sr = input()
# n = [sr] * a
# for i in range(a):
#     n[i] = [sr] * a
# print(n)

# for row in matrix:
#     print(*row)


# #4
# for i in range (1, 6):
#     for j in range(1,6):
#         print(f'{i} * {j} = {i * j}', end ='\t') 
#     print()


#5 
# size = 8
# for i in range (size):
#     for j in range(size):
#         symvol = "*" if (i + j) % 2==0 else '.'
#         print(symvol, end = ' ')
#     print()

#6
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # list1 = []
# # for i in a:
# #     if i > 5:
# #         list1.append(i)
# # print(list1)
# new = [i for i in a if i >5]
# print(new)
    
#7
# new = [i for i in range (1900, 2024) if (i % 4 == 0) and not (i != 100 )]
# print(f' Год высокосный: ', *new)

# #8
# n = int(input())
# for i in (1, n):
#     for j in range(1,10):
#         print((i*j), end = ' ')
#     print()

# for i in range (1,11):
#     print(f)
#9
# a = 1 
# s = 0
# while a <= 30:
#     s = a + s
#     a = a + 1
# print(s)

#10 
# a = [10,30,40,20,50,100]
# if 20 in a:

# b = a.index(20)
# b2 = a.pop(b)
# c = a.insert(b, 200)

# a[b]=200
# print(a)


#11 
# a = [1,2,3,4,5]
# list_comp = [i ** 2 for i in a]
# print(list_comp)

#12
# a = [1,2,3,4,5,6,7,8,9]
# index = len(a) - 1
# new = []
# while index >= 0:
#     new.append(a[index])
#     index -= 1
# print(new)
#13
# 
# a = 3
# b = -11
# c = -2
# possitivw = [num for num in [a,b,c] if num >0]
# print(possitivw)

# month = int(input())

