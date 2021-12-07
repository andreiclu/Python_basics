import time
import os

while True:
    if os.path.exists("vegetables.txt"):

        with open ("vegetables.txt") as file:
            print (file.read())

    else: 
        print("File does not exist:")
        
    time.sleep(10)
