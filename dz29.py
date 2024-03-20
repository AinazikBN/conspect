#5 
# list1 = ["ghjlerns", 1,4,2,6 ]
# list2 = ["dcuebcwu", 3,4,56 ]
# list1.extend(list2)
# print(list1) 

#6 
# l = ['Sanjar', 'Tilek', 'Kalys', 'Eldar', 'Elina', 'Beka', 'Elzar', 'Bael', 'Atajan', 'Emir', 'Mamed', 'Beka']
# print(l.count("Beka"))

#7 
# l = ['Sanjar', 'Tilek', 'Kalys', 'Eldar', 'Elina', 'Beka', 'Elzar', 'Bael', 'Atajan', 'Emir', 'Mamed', 'Beka']
# l.remove("Elina")
# print(l)

#8
# list1 = []
# list1.append({'Ainazik', 2006, "Python"})
# print(list1)

#9
# l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']
# l.remove("loop")
# print(l)

#10 
# l = [1, 2, 5, 3]
# a,b,c,d = l
# print(a * b * c *d)


# l = [1, 2, 5, 3]
# a = 1 
# for i in l:
#     a *= i
# print(i)

#11 
# s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples'
# numbers = []
# letters = []
# for i in s:
#     if i.isdigit():
#         numbers += i
# print ("".join(numbers))
# for i in s:
#     if i.isalpha():
#         letters += i
# print(''.join(letters)) 

#12
# l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']
# l1 = [l.pop(0), l.pop(1), l.pop(2)]
# print(l1)

# print(l.pop(0), l.pop(0), l.pop(0))

# print(l[0:3])

# i = 1
# num = int(input())
# for i in range (0, num):
#     if num % i == 0:
#         i += 1
#     print (i)

# num = int(input())
# list1 = []
# for i in range (1, num+1):
#     if num % i == 0:
#         list1.append(i)
# print (list1)


# num = int(input())
# list_ = []
# for i in range (num):
#     string_ = input()
#     list_.append(string_)

# print(list_)

# a = ['a', 'b', 'c', 'd', 'e', 'f', ghijklmnopqrstuvwxyzv]
# a = "abcdefghijklmnopqrstuvwxyz"
# list_ = []
# for i in range (0, len(a)):
#     list_.append(a[i]* (i+1))
# print(list_)


num = int(input())
list_= []
for i in range (num):
    str_ = input()
    list_.extend(str_)
    list1 = list(list_)
print(list1)
    