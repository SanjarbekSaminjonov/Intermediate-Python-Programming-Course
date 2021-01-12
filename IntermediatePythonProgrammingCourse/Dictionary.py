# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {'name': 'Sanjarbek', 'lastname': 'Saminjonov', 'age': 19}
mydict_ = dict(name = 'Sanjarbek', lastname = 'Saminjonov', age = 19)

# print(mydict)
# print(mydict_)
# # printed:
# # {'name': 'Sanjarbek', 'lastname': 'Saminjonov', 'age': 19}
# # {'name': 'Sanjarbek', 'lastname': 'Saminjonov', 'age': 19}

############################################################################

mydict['email'] = 'sanjarbeksaminjonovv@gmail.com'
del mydict['age']
mydict.pop('name')
# print(mydict)
# # printed:
# # {'lastname': 'Saminjonov', 'email': 'sanjarbeksaminjonovv@gmail.com'}

##############################################################################

# for key, value in mydict.items():
#     print(key, value)

##############################################################################

mydict_ = mydict

ali = "ism"
mydict[ali] = "Ali"

# {'name': 'Sanjarbek', 'lastname': 'Saminjonov', 'age': 19, 'ism': 'Ali'}
# {'name': 'Sanjarbek', 'lastname': 'Saminjonov', 'age': 19, 'ism': 'Ali'}

################################################################################

a = {'name': 'Sanjarbek', 'age': 19, 'email': 'sanjarbek@mail.uz', 'region': 'Fergana'}
b = dict(name = 'Oybekjon', age = 20, email = 'sulaymonov@mail.uz', village = 'Qirqvolida')
# a.update(b)

# print(a)
# print(b)
# {'name': 'Oybekjon', 'age': 20, 'email': 'sulaymonov@mail.uz', 'region': 'Fergana', 'village': 'Qirqvolida'}
# {'name': 'Oybekjon', 'age': 20, 'email': 'sulaymonov@mail.uz', 'village': 'Qirqvolida'}

# b.update(a)

# print(a)
# print(b)
# {'name': 'Sanjarbek', 'age': 19, 'email': 'sanjarbek@mail.uz', 'region': 'Fergana'}
# {'name': 'Sanjarbek', 'age': 19, 'email': 'sanjarbek@mail.uz', 'village': 'Qirqvolida', 'region': 'Fergana'}

######################################################################################################

mytuple = (3, 5)
mydict = {mytuple: 4}
# print(mydict)
# {(3, 5): 4}

# but:
# mylist = [3, 5]
# mydict = {mylist: 4}
# # print(mydict)
# #     mydict = {mylist: 4}
# # TypeError: unhashable type: 'list'