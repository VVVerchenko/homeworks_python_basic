class DigitValidation(Exception):
    def __init__(self,num_list):
        self.n = num_list

n_list = []
i = 0
while True:
    current_num = input("Введите число, для завершения введите 'stop': ")
    if current_num != "stop":
        try:
            if current_num.isdigit() == False:
                raise DigitValidation('Необходимо ввести число!')
        except (ValueError, DigitValidation) as err:
            print(err)
        else:
            current_num = int(current_num)
            n_list.append(current_num)
        finally:
            pass
    else:
        print(f"\nВаш список:\n{n_list}")
        break