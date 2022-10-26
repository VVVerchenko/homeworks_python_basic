with open(r"task2_l5_text.txt", "r", encoding="utf-8") as my_f:
    my_f_list = my_f.read().split('\n')

print(f"Число строк в тексте: {len(my_f_list)}")
for i in range(len(my_f_list)):
    current_line_list = my_f_list[i].split(" ")
    current_words_amount = len(current_line_list)
    print(f"Количество слов в {i+1}-й строке: {current_words_amount}")




