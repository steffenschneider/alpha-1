import random

random.random()  # Random float x, 0.0 <= x < 1.0
# 0.37444887175646646

random.randrange(10)  # Integer from 0 to 9
# 7

random.randint(10, 12)  # Integer from 10 to 12

random.choice('abcdefghij')  # Single random element
# 'c'

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)  # [7, 3, 2, 5, 6, 4, 1]

random.sample([1, 2, 3, 4, 5], 3)  # Three samples without replacement
# [4, 1, 5]

weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
print(population)  # ['Red', 'Red', 'Red', 'Blue', 'Blue', 'Yellow', 'Green', 'Green', 'Green', 'Green']
random.choice(population)  # 'Green'
