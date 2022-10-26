translate_dict = {"One": "Один", "Two": "Два","Three": "Три","Four": "Четыре"}

with open("task4_l5_text.txt", "r", encoding="utf-8") as my_f:
    my_f_list = my_f.read().split("\n")

result_list = []
for i in range(len(my_f_list)):
    current_line_list = my_f_list[i].split(" ")
    current_word = current_line_list[0]
    current_result_list = [translate_dict[current_word],current_line_list[1],current_line_list[2]]
    current_result_str = " ".join(current_result_list)
    result_list.append(current_result_str)
result_str = "\n".join(result_list)

with open("task4_l5_text_res.txt", "w", encoding="utf-8") as my_r:
    my_r.write(result_str)

print(result_str)