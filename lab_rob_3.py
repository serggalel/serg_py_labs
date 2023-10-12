import random as r

my_array = []
for _ in range(5):
    my_array.append([r.randint(1, 99) for _ in range(5)])


def print_array(array):
    for row in array:
        for number in row:
            print(f'-{number:02}-', end=' ')
        print()
    print()


def print_array_with_check(array, check):
    for row in array:
        for number in row:
            if check >= number:
                print(f'-{number:02}-', end=' ')
            else:
                print(f'*{number:02}*', end=' ')
        print()
    print()


print_array(my_array)

print()


def func(array):
    while True:
        check = int(float(input("Введіть ціле число для цього  масиву: ")))
        if 0 < check < 99:
            print_array_with_check(array, check)
        else:
            print("Має бути від 1 до 98")
            print()


func(my_array)
