from sys import argv

production_in_hours, hourly_wage_rate, premium = map(float, argv[1:])
print(f"Заработная плата составляет: {production_in_hours * hourly_wage_rate + premium}")

# Пример ввода данных в терминал: python task1_l4.py 168 300 10000