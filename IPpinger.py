import colorama
import os
import time

def ipping():
    count = 1
    hostname = input("Enter IP here: ")
    os.system('cls')
    print("-"*100)
    print("="*100)
    print("-"*100)
    while True:
        response = os.system("ping -n 1 " + hostname + " >nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " is online!" + " [" +  str(count) + "]" +  '\033[0m')
        else:
            print("\033[31m" + hostname + " is offline!" " [" +  str(count) + "]" +  '\033[0m')
        count += 1
        time.sleep(2)

ipping()
