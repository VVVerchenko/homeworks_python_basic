def summa():
    summa = 0

    while True:
        numbers_str = input('Введите числа разделённые пробелами, для выхода введите "стоп": ')
        numbers_list_str = numbers_str.split()

        for i in range(len(numbers_list_str)):
            if numbers_list_str[i] == "стоп":
                numbers_list_int = list(map(int, numbers_list_str[:i]))
                for s in range(len(numbers_list_int)):
                    summa += numbers_list_int[s]
                print(f"Сумма: {summa}")
                return

        for s in range(len(numbers_list_str)):
            numbers_list_int = list(map(int,numbers_list_str))
            for s in range(len(numbers_list_str)):
                summa += numbers_list_int[s]
            print(f"Сумма: {summa}")
            break

summa()