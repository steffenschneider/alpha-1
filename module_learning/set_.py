## add
a_set = set()
a_set.add(1)
# print(a_set)  # {1}


## clear
b_set = set()
b_set.add(1)
b_set.add(2)
# print(b_set)    # {1, 2}
# print(b_set.clear())  # None


## difference


## discard


## intersection_update


## intersection


## isdisjoint


## issubset


## len


## pop


## remove


## symmetric_difference


## union
set_a = set(['1', '2'])
set_b = set(['3', '4'])
set_a.union(set_b)
# print(set_a)    # output   ???????????????????????
# set(['a', 'c', 'b', '1', '3', '2', '4'])


## update
# add values; also use value |= (1)
s = {1, 2, 3}
news = s | {4}
# print(s)       # {1, 2, 3}
# print(news)    # {1, 2, 3, 4}
# Note how s has remained unchanged.
s.update({4})
# print(s)       # {1, 2, 3, 4}
