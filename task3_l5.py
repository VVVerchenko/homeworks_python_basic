with open("task3_l5_text.txt", "r", encoding="utf-8") as my_f:
    my_f_list = my_f.read().split("\n")

print("Зарплату менее 20000р получают следующие сотрудники: ")
total_salary = 0

for i in range(len(my_f_list)):
    current_employee_list = my_f_list[i].split(" ")
    current_salary = float(current_employee_list[1])
    total_salary += current_salary
    if current_salary < 20000.00:
         print(current_employee_list[0])
    else: continue

awarage_salary = total_salary / len(my_f_list)

print("-" * 50)
print(f"Средняя зарплата всех сотрудников: {awarage_salary}")