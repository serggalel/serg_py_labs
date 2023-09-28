#Pershe zavdannya

a = int(float(input("Введіть число: ")))
if a < -999 or a > 999:
    print("Треба вказати число з указаного проміжку")
else:
    if -10 < a < 0:
        print(a, "є від'ємне однозначне число")
    elif -100 < a <= -10:
        print(a, "є від'ємне двозначне число")
    elif -999 < a <= -100:
        print(a, "є від'ємне тризначне число")
    elif 10 > a > 0:
        print(a, "є додатне однозначне число")
    elif 100 > a >= 10:
        print(a, "є додатне двозначне число")
    elif 999 > a >= 100:
        print(a, "є додатне тризначне число")
    elif a == 0:
        print(a, "є нульове число")







#Druhe zavdannya

n1 = int(float(input("Введіть n1: ")))
n2 = int(float(input("Введіть n2: ")))
k = n1
sum = 0

if 1 <= n1 <= n2:
    for k in range(n1, n2 + 1):
        sum += (((-1)**(k - 1))*3**k)/(k)
    print(sum)
else:
    print("Error")







