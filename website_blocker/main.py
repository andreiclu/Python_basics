import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect ='127.0.0.1'
website_list=['www.facebook.com', "facebook.com", 'www.instagram.com','instagram.com', 'www.youtube.com','youtube.com']

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,11) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,21):
        print("Working hours...")
    else:
        print("Fun hours...")



    time.sleep(5)
