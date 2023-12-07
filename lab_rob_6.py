import math

while True:
    print("\nЗагальний вигляд квадратного рівняння:\nax^2 + bx + c = 0\nОтже введіть a, b і c:")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    print(f"Отже зараз ваше рівняння виглядає ось так:\n{a}*x^2 + {b}*x + {c} = 0")

    D = math.pow(b, 2) - 4*a*c
    if D < 0:
        print("Немає коренів")
        continue
    elif a == 0 and b != 0:
        x1 = x2 = -c/b
    elif a == b == c == 0:
        print("Рівняння має безліч коренів")
        continue
    elif a == 0 and b == 0 and c != 0:
        print("Немає коренів")
        continue
    else:
        x1 = 0.5 * (-b + math.sqrt(D))
        x2 = 0.5 * (-b - math.sqrt(D))

    print(f"Отже ваші корені: {x1:.02} та {x2:.02}")

    file = open("LAB6.txt", "a", encoding='UTF-8')
    file.write(f"\nРівняння: {a}*x^2 + {b}*x + {c} = 0\nЙого корені: {x1:.02} та {x2:.02}\n")