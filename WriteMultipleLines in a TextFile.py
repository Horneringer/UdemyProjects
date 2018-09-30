numbers = [1, 2, 3]
file = open(r"D:\PyCharm\Projects\Udemy\list.txt", "w")
for item in numbers:
    file.write(str(item) + '\n')
file.close()

