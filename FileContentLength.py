file = open(r"D:\PyCharm\Projects\Udemy\fruits.txt")
cont = file.read()
cont_list = cont.splitlines()
file.close()

for item in cont_list:
    length = len(item)
    print(length)