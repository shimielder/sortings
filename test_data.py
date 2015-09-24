from random import randint
from timeit import timeit

from insertion import insertion_sort
from bubble import bubble_sort
from quick import quick_sort, qsort

size=1000
tests_count=100
funcs = [bubble_sort, insertion_sort, quick_sort, qsort, sorted]
x = []
y = []
z = []
tests = [x, y, z]

for i in range(size):
    x.append(chr(randint(48, 122)))

for k in range(size):
    y.append('')
    for j in range(randint(1, 9)):
        y[k] += chr(randint(48, 122))

for l in range(size):
    z.append(randint(0, 1000))



print('Set #1: ', x)
print('Set #2: ', y)
print('Set #3: ', z)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


for func in funcs:
    for test in tests:
        print('Preparing {}...'.format(func.__name__))
        sort_test = wrapper(func, test)
        print('Done')
        print('{} time:'.format(func.__name__), timeit(sort_test, number = tests_count))



