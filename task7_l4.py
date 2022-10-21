n = int(input("Введите число для вычисления факториала: "))

def gen(n):
    f_num = 1
    for i in range(n + 1):
        yield f"Факториал {i} = {f_num}"
        f_num *= i + 1

for e in gen(n):
    print(e)
