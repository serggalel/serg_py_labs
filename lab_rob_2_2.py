# Variant - 4

deposit = float(input("Введіть суму депозиту: "))
annual = float(input("Введіть річні відсотки: ")) / 100
months = int(float(input("Введіть тривалість депозиту у місяцях: ")))

if 0 < annual < 100 and months > 0 and deposit > 0:
    for month in range(1, months + 1):
        earned = deposit * (annual / 12)
        deposit += earned
        print(f"Місяць {month}: загальна сума вкладу = {deposit:.2f} ; нараховані відсотки = {earned:.2f}")
else:
    print("Помилка! Будь ласка, введіть коректні дані.")
