text = input("Введите текст из маленьких латинских букв: ")

def int_func(t):
    text_to_list_for_cheking = text.split()
    checking = []
    for i in range(len(text_to_list_for_cheking)):
        checking.append(text_to_list_for_cheking[i])
    for e in range(len(checking)):
        for w in range(len(checking[e])):

            if ord(checking[e][w]) < 97 or ord(checking[e][w]) > 122:
                return "Нужно было ввести текст из меленьких латинских букв, перезапустите программу"
            else: continue
    t = text.title()
    return t

print(int_func(text))