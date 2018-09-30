import time
from datetime import datetime as dt

host_temp = 'hosts'
host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
websites_list = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'twitter.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          16):
        print('Работай! Солнце ещё высоко...')
        with open(host_temp, 'r+') as file:
            cont = file.read()
            for website in websites_list:
                if website in cont:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    
    else:
        with open(host_temp, 'r+') as file:
            cont = file.readlines()
            file.seek(0)
            for line in cont:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print('Гуляй, Вася!')
    time.sleep(5)
