import json

with open("task7_l5_text.txt","r", encoding="utf-8") as my_f:
    my_f_str = my_f.read()

my_f_list = my_f_str.split("\n")
total_dict_profit = {}
avarage_profit_dict = {}
total_company_profit = 0
total_company_profit_for_avarage = 0
amount_of_profitable_companies = 0

for i in range(len(my_f_list)):
    current_company_list_str = my_f_list[i].split()
    current_company_list_int = list(map(int, current_company_list_str[2:4]))
    current_company_name = " ".join(current_company_list_str[0:2])
    current_company_profit = current_company_list_int[0] - current_company_list_int[1]

    if current_company_profit > 0:
        total_company_profit_for_avarage += current_company_profit
        amount_of_profitable_companies += 1
    else: pass
    total_dict_profit[current_company_name] = current_company_profit

avarage_profit_dict["avarage_profit"] = round(total_company_profit_for_avarage / amount_of_profitable_companies, 2)
total_list = [total_dict_profit, avarage_profit_dict]
j_total_list = json.dumps(total_list, ensure_ascii=False)

with open("task7_l5_text_j.json", "w", encoding="utf-8") as my_j:
    my_j.write(j_total_list)

