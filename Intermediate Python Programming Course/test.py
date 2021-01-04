# a = [1, 3, 5]
# b = [2, 4, 6]

# ab = list(map(lambda x, y: x + y, a, b))
# print(ab) # [3, 7, 11]

#################################################################

# from random import random, choice, sample

# sonlar = sample(range(100), 10)
# print(type(sonlar)) # <class 'list'>

# def juft(n):
#     '''sonning juftligini tekshiruvchi funfsiya'''
#     return n % 2 == 0

# juft_sonlar1 = list(filter(juft, sonlar))
# juft_sonlar2 = list(filter(lambda n: n % 2 == 0, sonlar))
# print(juft_sonlar1)
# print(juft_sonlar2)
# print('salom'.upper())