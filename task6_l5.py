with open("task6_l5_text.txt", "r", encoding="utf-8") as my_f:
    my_f_list_str = my_f.read().split("\n")

result_dict = {}
for i in range(len(my_f_list_str)):
    current_list = my_f_list_str[i].split(":")
    subject = current_list[0] # название дисциплины
    current_list2 = []
    current_sum = 0

    for n in range(len(current_list[1])):
        if (ord(current_list[1][n]) >= 48 and ord(current_list[1][n]) <= 57) or ord(current_list[1][n]) == 32:
            current_list2.append(current_list[1][n])
            current_list3_int = list(map(int, "".join(current_list2).split()))
        else:continue

    for s in range(len(current_list3_int)):
        current_sum += current_list3_int[s] # количество занятий по текущей дисциплине

    result_dict[subject] = current_sum
print(result_dict)
