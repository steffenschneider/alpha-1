from itertools import *

## chain
for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i)


## cycle
i = 0
for item in cycle(['a', 'b', 'c']):
    i += 1
    if i == 10:
        break
    print(i, item)

# todo
## imap
for i in imap(lambda x, y: (x, y, x * y), repeat(2), xrange(5)):
    print('%d * %d = %d' % i)

# todo
## izip
print("")
for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print(i)

## repeat
for i in repeat('over-and-over', 5):
    print(i)
