# Tuples: ordred, mutable, allows duplicate elements

mytuple = (5, 2, 'apple')
# printed - (5, 2, 'apple')

mytuple = ("max")
# printed - max
# type(mytuple) is str

########################################################################

mytuple = ('a', 'p', 'p', 'l', 'e')

my_list = list(mytuple)
# my_list = ['a', 'p', 'p', 'l', 'e']

my_tuple = tuple(my_list)
# my_tuple = ('a', 'p', 'p', 'l', 'e')

#########################################################################

mytuple = (1, 'apple', True)
a, b, c = mytuple
# a = 1
# b = 'apple'
# c = True

mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple
# i1 = 0
# i2 = [1, 2, 3]
# i3 = 4

###########################################################################

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
# print(sys.getsizeof(my_list), 'bytes')  # printed 120 bytes
# print(sys.getsizeof(my_tuple), 'bytes')  # printed 80 bytes