file = open("LAB.txt", "r")
file_text = file.read()
file_arr = file_text.split("\n")

print("Our file:")
print(file_text)

value = 0
for i in file_arr:
    try:
        j = i.split(" -- ")
        value += float(j[1])
    except:
        print("ERROR")

print(f"The value of all goods in list: {value}")
