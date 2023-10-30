class Smartphone:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def count_years(self):
        current_year = int(float(input("Enter current year: ")))
        return f"Smartphone '{self.name}' is {int(float(current_year)) - self.year} years old"

    def __str__(self):
        return f"{self.name}, {self.year}"


class Shop:

    def __init__(self):
        self.smartphones = []

    def add_smartphone(self):
        name = input("Enter smartphone's name: ")
        year = int(input("Enter smartphone's year: "))
        new_smartphone = Smartphone(name, year)
        self.smartphones.append(new_smartphone)

    def delete_smartphone(self, name):

        for i in self.smartphones:
            if i.name == name:
                self.smartphones.remove(i)

    def show_list(self):
        print()
        print("List of smartphones:")
        for i in self.smartphones:
            print(i.name, i.year)

    def show_new(self, year):
        print()
        print("List of smartphones that are new:")
        for i in self.smartphones:
            if i.year >= year:
                print(i.name, i.year)


sh = Shop()
while True:
    x = int(input("Enter what do you want:\n"
                  "1 - count how old smartphone is\n"
                  "2 - add a new smartphone\n"
                  "3 - delete smartphone\n"
                  "4 - show all smartphones\n"
                  "5 - show only new smartphones\n"
                  "0 - exit\n"))

    if x == 1:
        name = input("Enter smartphone's name: ")
        year = int(input("Enter smartphone's year: "))
        sm = Smartphone(name, year)
        print(sm.count_years())
    if x == 2:
        sh.add_smartphone()
    if x == 3:
        name = input("Enter smartphone's name: ")
        sh.delete_smartphone(name)
    if x == 4:
        sh.show_list()
    if x == 5:
        year = int(input("Enter current year: "))
        sh.show_new(year)
    if x == 0:
        print("Goodbye!")
        break
    if x > 5 or x < 0:
        print("Error")
