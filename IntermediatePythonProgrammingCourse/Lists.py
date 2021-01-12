# List: ordred, mutable, allows duplicate elements

mylist = ['banana', 'cherry', 'apple']

item = mylist[-1]
# item = 'apple'

##############################################################################

if 'banana' in mylist:
    item = 'yes'
else:
    item = 'no'
# item = 'yes'

item = len(mylist)
# item = 3

mylist.append('lemon')
# mylist = ['banana', 'cherry', 'apple', 'lemon']

mylist.insert(1, 'blueberry')
# mylist = ['banana', 'blueberry', 'cherry', 'apple', 'lemon']

item = mylist.pop()
# item = 'lemon' (this is last element)
# mylist = ['banana', 'blueberry', 'cherry', 'apple']

mylist.remove('cherry')
# mylist = ['banana', 'blueberry', 'apple']

mylist.reverse()
# mylist = ['apple', 'blueberry', 'banana']

mylist.clear()
# mylist = []

##################################################################################

mylist = [3, 4, -1, 1, 8, -6]

newlist = sorted(mylist)
# mylist = [3, 4, -1, 1, 8, -6]
# newlist = [-6, -1, 1, 3, 4, 8]

mylist.sort()
# mylist = [-6, -1, 1, 3, 4, 8]

mylist1 = [0] * 5
# mylist = [0, 0, 0, 0, 0]

mylist2 = [1, 2, 3, 4]
mylist = mylist1 + mylist2
# mylist = [0, 0, 0, 0, 0, 1, 2, 3, 4]

#################################################################################

mylist = [1, 2, 3, 4, 5, 6, 7, 8]

item = mylist[1:5]
# item = [2, 3, 4, 5]

item = mylist[::1]
# item = [1, 2, 3, 4, 5, 6, 7, 8]

item = mylist[::2]
# item = [1, 3, 5, 7]

item = mylist[::-1]
# item = [8, 7, 6, 5, 4, 3, 2, 1] (reverse)

#######################################################################

list_org = ['banana', 'cherry', 'apple']
list_cpy = list_org
# list_org = ['banana', 'cherry', 'apple']
# list_cpy = ['banana', 'cherry', 'apple']

list_cpy.append('lemon')
# list_org = ['banana', 'cherry', 'apple', 'lemon']
# list_cpy = ['banana', 'cherry', 'apple', 'lemon']

list_cpy = [1, 4]
# list_org = ['banana', 'cherry', 'apple']
# list_cpy = [1, 4]

list_org = ['banana', 'cherry', 'apple']
list_cpy = list(list_org) # or  = list_org.copy() or  = list_org[:]
# list_org = ['banana', 'cherry', 'apple']
# list_cpy = ['banana', 'cherry', 'apple']

list_cpy.append('lemon')
# list_org = ['banana', 'cherry', 'apple']
# list_cpy = ['banana', 'cherry', 'apple', 'lemon']

####################################################################################

mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = [i * i for i in mylist1]
# mylist1 = [1, 2, 3, 4, 5, 6]
# mylist2 = [1, 4, 9, 16, 25, 36]

#####################################################################################

mylist1 = [1, 5, 7, 1]
mylist2 = ['banana', 'apple', 'cherry']
mylist = mylist1 + mylist2

# mylist.sort() (TypeError: '<' not supported between instances of 'str' and 'int')
mylist1.sort()
mylist2.sort()
# mylist1 = [1, 1, 5, 7]
# mylist2 = ['apple', 'banana', 'cherry']
# mylist.sort() (TypeError: '<' not supported between instances of 'str' and 'int')

print(mylist)