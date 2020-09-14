import time
from datetime import datetime as dt

hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  # make the file path to \hosts to try it first
hosts_temp = "hosts"  
redirect = "127.0.0.1"
blocked_website_list = ["www.facebook.com", "facebook.com"] # you can add more websites if you want

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("We should work now !!")
        with open(hosts_path, 'r+') as file:  
            content = file.read()
            for website in blocked_website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "  " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()  
            file.seek(0)  
            for line in content:
                if not any(website in line for website in blocked_website_list):
                    
                    file.write(line)
                file.truncate()
        print("Let's take a break")

    time.sleep(4)
