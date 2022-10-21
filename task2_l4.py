first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
second_list = [first_list[i] for i in range(len(first_list)) if first_list[i] > first_list[i-1] and i!=0]
print(second_list)

