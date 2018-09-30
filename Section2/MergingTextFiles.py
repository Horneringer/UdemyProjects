import datetime

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f.txt"), 'a+') as file_4:
    with open(r'D:\PyCharm\Projects\Udemy\file1.txt', 'r') as file_1:
        cont1 = file_1.read()
    
    for item in cont1:
        file_4.write(item)
    file_4.write('\n')
    
    with open(r'D:\PyCharm\Projects\Udemy\file2.txt', 'r') as file_2:
        cont2 = file_2.read()
    
    for item in cont2:
        file_4.write(item)
    file_4.write('\n')
    
    with open(r'D:\PyCharm\Projects\Udemy\file3.txt', 'r') as file_3:
        cont3 = file_3.read()
    
    for item in cont3:
        file_4.write(item)
    file_4.write('\n')

# --------------------------------------------- рациональный вариант-----------------------------------------------------

'''
import glob2
from datetime import datetime

filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")


'''


