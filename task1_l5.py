while True:
    input_text = input("Введите текст или пустую строку для завершения: ")
    if input_text != "":
        with open("task1_l5_text_res.txt", "a", encoding= "utf-8") as my_f:
            my_f.write(f"{input_text}\n")
    else: break