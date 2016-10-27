# coding=utf-8

## reverse
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.reverse())  # None !!!
# reverse() reverses the elements of the list, in place.
# You might have noticed that methods like insert,
# remove or sort that only modify the list have no
# return value printed – they return the default None.
# This is a design principle for all mutable data
# structures in Python.
print(lst)  # ['e', 'd', 'c', 'b', 'a']

## pop
lst = ['a', 'b', 'c', 'd', 'e']
elem_at_3 = lst.pop(3)  # remove item at position
print(lst)  # ['a', 'b', 'c', 'e']
print(elem_at_3)  # d

## remove
lst = ['a', 'b', 'c', 'd', 'e']
lst.remove('e')  # remove item 'e'

## insert
lst = ['a', 'b', 'c', 'e']
lst.insert(3, 'd')  # insert 'd' at fourth position
print(lst)  # ['a', 'b', 'c', 'd', 'e']

## append
# append one item
lst = ['a', 'b', 'c', 'd', 'e']
lst2 = ['1', '2']
lst.append(lst2)
print(lst)  # ['a', 'b', 'c', 'd', 'e', ['1', '2']]

## extend
# concatenate two lists
lst = ['a', 'b', 'c', 'd', 'e']
lst2 = ['1', '2']
lst.extend(lst2)
print(lst)  # ['a', 'b', 'c', 'd', 'e', '1', '2']
