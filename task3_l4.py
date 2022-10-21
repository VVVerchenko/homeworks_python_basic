first_list = list(range(20, 241))
second_list = [i for i in first_list if i % 20 == 0 or i % 21 == 0]
print(second_list)