print("ЛР №1 Базові математичні операції")
print("Галелюк Сергій КІ-2")
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
d=float(input("d= "))
print(a+b/c**d)


x=2.8
print(int(x))
s1="2.3"
s2="2,3"
#print(int(s1))  --  виникає помилка
print(int(float(s1)))
#print(int(float(s2)))  --  також виникає помилка


a=10
b=2.4
print(a, b)
print(a, b, sep='|')
print(a, b, sep='*')
#розділювач : 10*2.4
print(a, b, sep='\n')
#             ↑↑↑↑   переводить на наступний рядок
print(a, b, sep='\t')
# табуляція   ↑↑↑↑ : 10 2.4
print(a, b, end='     wseffws')
#у кінці додає : 10 2.4     wseffws

print("")
#n=int(input("n="))  --  помилка
n=int(float(input("n=")))
print(n)


#Calculator:

first_number=float(input("перше число: "))
second_number=float(input("друге число: "))
equals="="

print(first_number, "+", second_number, equals, first_number + second_number)
print(first_number, "-", second_number, equals, first_number - second_number)
print(first_number, "*", second_number, equals, first_number * second_number)
print(first_number, "/", second_number, equals, first_number / second_number)
print(first_number, "//", second_number, equals, first_number // second_number)
print(first_number, "**", second_number, equals, first_number ** second_number)