from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

print("-" * 20)
list1 = ["A", "B", "C", "D", "E", "F"]
n = 0
for i in cycle(list1):
    if n >= 10:
        break
    else:
        print(i)
    n += 1
