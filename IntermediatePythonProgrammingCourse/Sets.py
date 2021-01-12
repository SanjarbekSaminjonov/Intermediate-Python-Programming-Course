# # Sets: unordered, mutable, no dublicates

# myset = {1, 2, 3, 1, 3}
# print(myset) # {1, 2, 3}

# myset = set((1, 3, 4, 3, 2))
# print(myset) # {1, 2, 3, 4}

# myset = set("hello")
# print(myset) # {'e', 'h', 'o', 'l'}

# myset = set()
# myset.add('hello')
# myset.add(25)
# myset.add(True)
# myset.add(2)
# myset.remove(True)
# print(myset) # {25, 2, 'hello'}
# myset.remove(5) # KeyError: 5

# myset = {1, 2, 3}
# myset.discard(3)
# print(myset) # {1, 2}

# myset = {1, 2, 3}
# myset.discard(4)
# print(myset) # {1, 2, 3}

# myset = {1, 2, 3, 4}
# myset.clear()
# print(myset) # set()

# myset = {1, 2, 3, 4}
# print(myset.pop()) # 1
# print(myset) # {2, 3, 4}

#######################################################################################

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens) # odds + evens
# # print(u) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# i = odds.intersection(evens) # ikkisida bor elementlar
# # print(i) # set()

# i = odds.intersection(primes)
# # print(i) # {3, 5, 7}

####################################################################################

# setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {0, 1, 2, 3, 4, 5, 10, 11, 12, 13}

# # diffA = setA.difference(setB) # setA dan setB ning ayirmasi
# # # print(diffA) # {8, 9, 6, 7}
# # diffB = setB.difference(setA)
# # # print(diffB) # {11, 12, 13}

# # diff = setA.symmetric_difference(setB)
# # print(diff) # {6, 7, 8, 9, 11, 12, 13}

#########################################################################

# setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {0, 1, 2, 3, 4, 5, 10, 11, 12, 13}

# # listA = list(setA)
# # # print(listA) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # tupleB = tuple(setB)
# # # print(tupleB) # (0, 1, 2, 3, 4, 5, 10, 11, 12, 13)

# # # dictA = dict(setA)
# # # print(dictA) # TypeError: cannot convert dictionary update sequence element #0 to a sequence

#####################################################################################

# setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {0, 1, 2, 3, 4, 5, 10, 11, 12, 13}

# u = setA.union(setB)
# # print(u) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# setA.update(setB)
# # print(setA) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

########################################################################################

# setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {0, 1, 2, 3, 4, 5, 10, 11, 12, 13}

# i = setA.intersection(setB)
# # print(i) # {0, 1, 2, 3, 4, 5, 10}

# setA.intersection_update(setB)
# # print(setA) # {0, 1, 2, 3, 4, 5, 10}

#######################################################################################

# setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {0, 1, 2, 3, 4, 5, 10, 11, 12, 13}

# setA.difference_update(setB)
# # print(setA) # {6, 7, 8, 9}

#######################################################################################

# setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setB = {0, 1, 2, 3, 4, 5, 10, 11, 12, 13}

# setA.symmetric_difference_update(setB)
# # print(setA) # {6, 7, 8, 9, 11, 12, 13}

######################################################################################

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {6, 7}
# print(set1.issubset(set2)) # True
# print(set2.issubset(set1)) # False
# print(set1.issuperset(set2)) # False
# print(set2.issuperset(set2)) # True
# print(set1.isdisjoint(set2)) # False
# print(set2.isdisjoint(set1)) # False
# print(set1.isdisjoint(set3)) # True
# print(set2.isdisjoint(set3)) # True
# print(set3.isdisjoint(set1)) # True