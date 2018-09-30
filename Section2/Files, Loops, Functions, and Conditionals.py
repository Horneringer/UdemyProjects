temperatures = [10, -20, -289, 100]


def c_to_f(c):
    if c > -273.15:
        f = c * 9 / 5 + 32
        return f


with open(r"D:\PyCharm\Projects\Udemy\temperatures.txt", "w") as file:
    for t in temperatures:
        file.write(str(c_to_f(t)) + "\n")


#----------------------------------или можно сделать так---------------------------------------

'''temperatures = [10, -20, -289, 100]


def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")


writer(temperatures, "temps.txt")'''