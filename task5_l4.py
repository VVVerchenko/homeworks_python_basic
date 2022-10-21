from functools import reduce

list1 = list(range(100,1001,2))
def my_func(el1, el2):
    return el1 * el2

print(reduce(my_func, (list1)))