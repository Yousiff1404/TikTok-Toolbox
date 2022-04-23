from Report.report import TikTok_Report
import os
import time
from verify import TikTok_verify
from Logger import Logger

def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        pass

def main():
    clear()
    print("1. Tiktok Report Bot \n")
    choice = input("Enter your choice: ")

    if choice == "1":
        clear()

        username = input("Please enter the username of the account (without the @): ")
        id = input("Please enter the video ID (can be found in the URL): ")
        num = int(input("Please enter how many reports you would like to send: "))
        clear()

        if TikTok_verify.verifyVideo(username, id) == True:
            for i in range(num):
                TikTok_Report.sendRequest(username, id, i)
                time.sleep(5)
        else:
            Logger.error("Could not verify that the video is real...")
            input("Press any key to go back to the main menu")
            main()






    else:
        clear()
        main()

main()