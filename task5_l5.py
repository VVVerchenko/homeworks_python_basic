numbers_list_int = [1, 22, 23, 4, 66, 3, 2, 67, 1, 93]
numbers_list_str = list(map(str, numbers_list_int))
numbers_str = " ".join(numbers_list_str)
with open("task5_l5_text_res", "w", encoding="utf-8") as my_f:
    my_f.write(numbers_str)

with open("task5_l5_text_res", "r", encoding="utf-8") as my_r:
    read_str = my_r.read()

read_list_str = read_str.split(" ")
read_list_int = list(map(int, read_list_str))
sum = 0
for i in range(len(read_list_int)):
    sum += read_list_int[i]
print(f"Сумма чисел равна: {sum}")