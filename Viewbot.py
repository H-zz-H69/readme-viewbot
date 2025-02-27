import requests
from bs4 import BeautifulSoup
import time
import random
import threading
from colorama import init, Fore
import re

init(autoreset=True)

# Change this to ur View count URL
URL = "https://camo.githubusercontent.com/e4b90feb0a8cc3e31fbf1962b1f05a16c6b406b69700bb50a38d97f0dca84ab8/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d682d7a7a2d683639266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174"

session = requests.Session() 

def viewc():
    try:
        response = session.get(URL, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text_elements = soup.find_all("text")
            
            for element in text_elements:
                text = element.get_text(strip=True)
                if "Profile views" in text: 
                    continue
                numbers = re.findall(r"\d+", text) 
                if numbers:
                    return int("".join(numbers)) 

        return None
    except requests.RequestException:
        return None

def send_request():
    try:
        response = session.get(URL, timeout=5)
        if response.status_code == 200:
            print(Fore.MAGENTA + f"[H-zz-H]$- {Fore.GREEN}[+] Success")
        elif response.status_code == 429:
            print(f"{Fore.MAGENTA}[H-zz-H]$- {Fore.LIGHTRED_EX}[!] Rate limit reached. Waiting...")
            time.sleep(5)  
        else:
            print(f"{Fore.MAGENTA}[H-zz-H]$- {Fore.LIGHTRED_EX}[!] Failed to open the website. HTTP Status code:", response.status_code)
    except requests.RequestException:
        print(f"{Fore.MAGENTA}[H-zz-H]$- {Fore.RED}[!] Request failed.")

def requ():
    request_count = 0
    last_checked_count = 0

    def reqth(num_threads=5):
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    while True:
        reqth()

        request_count += 5

        if request_count % 50 == 0:
            current_count = viewc()
            if current_count is not None and current_count // 10 > last_checked_count // 10:
                ascii_art = """
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@
                                                @@@@@@@@%%%###%%%%%%%%%%%%%%%%%%@@@@@@@
                                                @@@@@@%%%--=-----=%%%%%=------:#%@@@@@@
                                                @@@@@%%%#-=%%%%#:=%%%%%=#%%%%+:#%%@@@@@
                                                @@@@%%%*+-=%%%%#:=%%%%%-#%%%%+:#%%@@@@@
                                                @@@@%%%--+=====--------=%%%%%+:#%%@@@@@
                                                @@@@%%%--%%%%%%%%%%%%%%%%%%%%=:#%%%@@@@
                                                @@@@%%%--%%%%%%%%%%%%%%%%%%%%=:#%%%@@@@
                                                @@@@%%%%*-=**+++++++*++=====++++:%%@@@@
                                                @@@@@%%%#-+%%%%%%%%%%%%%%%%%%%%#:%%@@@@
                                                @@@@@%%%#-+%%%%%###%%%%#%%#####*-%%@@@@
                                                @@@@@%%%#-+%%%%*:------:-------*#%%@@@@
                                                @@@@@@%%#-+%%%%*:+%%%%#-%%%%#=-%%%%@@@@
                                                @@@@@@%%#-+%%%%*:+%%%%#-%%%%%=-%%%@@@@@
                                                @@@@@@%%#-+%%%%*:+%%%%#-%%%%%=-%%%@@@@@
                                                @@@@@@@%#-=++++=:+%%%%#-*****--%%@@@@@@
                                                @@@@@@@@%#*******#%%%%%***++++*%@@@@@@@
                                                @@@@@@@@@@@%%%%%%%%@@@%%%%%%%@@@@@@@@@@
                                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                    Thanks for using our Service!
                                                                H-zz-H """
                print(ascii_art)
                print(Fore.MAGENTA + f"[H-zz-H]$- {Fore.GREEN}[+] Reached {current_count} views after {request_count} requests!")
                last_checked_count = current_count

        rate = random.uniform(0.05, 0.2)
        print(f"{Fore.MAGENTA}[H-zz-H]$- {Fore.YELLOW}[!] Waiting for {rate:.2f} seconds before next batch...\n")
        time.sleep(rate)

if __name__ == "__main__":
    requ()
