name = input("Введите ваше имя: ")
soname = input("Введите вашу фамилию: ")
year_of_birth = input("Введите ваш год рождения: ")
city = input("Введите город вашего проживания: ")
email = input("Введите ваш email: ")
phone_number = input("Введите ваш номер телефона: ")


def user_data(n, s, yb, c, em, pn):
    print(f"Ваши данные: {s} {n}, родились в {yb} году, проживаете в городе {c}, ваш email - {em}, тел. {pn}")

user_data(pn = phone_number, em = email, c = city, yb = year_of_birth, s = soname, n = name)