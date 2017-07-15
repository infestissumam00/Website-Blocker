import time
from datetime import datetime as dt

host_temp = "hosts"
host_path =r"C:\Windows\System32\Drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.yahoo.com","yahoo.com",]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
        print("Workin Hours")
        with open(host_temp,'r+') as file:
            co = file.read()
            for website in website_list:
                if website in co:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
    else:
        with open(host_temp,'r+') as file:
            co = file.readlines()
            file.seek(0)
            for line in co:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)
