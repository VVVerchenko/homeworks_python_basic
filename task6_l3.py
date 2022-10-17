word = input("Введите слово из маленьких латинских букв: ")

def int_func(t):
    checking = []
    for i in range(len(word)):
        checking.append(word[i])
    for e in range(len(checking)):
        if ord(checking[e]) < 97 or ord(checking[e]) > 122:
            return "Нужно было ввести слово из меленьких латинских букв, перезапустите программу"
        else: continue
    t = word.title()
    return t

print(int_func(word))
