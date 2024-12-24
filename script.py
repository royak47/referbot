import os
import sys
import random
import string
import time
import requests

# Function to print line
def linex():
    print('\033[0m================================================')

# Logo with banner and gradient colors
logo = f"""
\x1b[38;5;196m -================= ≫ ──── ≪•◦ ❈ ◦•≫ ──── ≪=================-\033[0m
\x1b[38;5;202m │                                                          │
\x1b[38;5;208m │  \x1b[38;5;196m██████╗  \x1b[38;5;202m█████╗ \x1b[38;5;208m██████╗ \x1b[38;5;214m██╗  ██╗                        │
\x1b[38;5;220m │  \x1b[38;5;208m██╔══██╗\x1b[38;5;202m██╔══██╗\x1b[38;5;196m██╔══██╗\x1b[38;5;220m██║ ██╔╝                        │
\x1b[38;5;190m │  \x1b[38;5;226m██║  ██║\x1b[38;5;190m███████║\x1b[38;5;154m██████╔╝\x1b[38;5;118m█████╔╝                         │
\x1b[38;5;82m  │  \x1b[38;5;118m██║  ██║\x1b[38;5;154m██╔══██║\x1b[38;5;190m██╔══██╗\x1b[38;5;226m██╔═██╗                         │
\x1b[38;5;220m │  \x1b[38;5;208m██████╔╝\x1b[38;5;202m██║  ██║\x1b[38;5;196m██║  ██║\x1b[38;5;220m██║  ██╗                        │
\x1b[38;5;214m │  \x1b[38;5;196m╚═════╝ \x1b[38;5;202m╚═╝  ╚═╝\x1b[38;5;208m╚═╝  ╚═╝\x1b[38;5;214m╚═╝  ╚═╝                        │
\x1b[38;5;190m │                                                          │
\x1b[38;5;154m │                                                          │
\x1b[38;5;118m ╰─━━━━━━━━━━━━━━━━━━━━━━━━Termux-os━━━━━━━━━━━━━━━━━━━━━━━─╯
\033[0m================================================
 \033[1;35m        Developer : Dark Life 🧬 
         Tele channel   : @scripthub00
         Tele group  : @scripthub0
\033[0m================================================
"""

# Display the logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
    print(logo)

# Password protection
def verify_password():
    correct_password = "darkwithX"
    print("\033[0m>>\033[1;32m Enter the password to access this script: \033[0m", end="")
    entered_password = input()
    if entered_password != correct_password:
        print("\033[1;31m⚠️ Incorrect password! Exiting...\033[0m")
        sys.exit()
    else:
        print("\033[1;32m>> Password correct! Proceeding...\033[0m")
        time.sleep(1)

# Display the progress in a chamber-like box
def display_progress(success_crt, reff_limit, atm):
    progress_bar = "#" * int((atm + 1) / reff_limit * 50) + " " * (50 - int((atm + 1) / reff_limit * 50))
    print(f"""
\033[1;36m ╔═════════════════════════════════════════════════════════╗
\033[1;32m ║  🟢 Current Progress      : {atm + 1}/{reff_limit} ({((atm + 1) / reff_limit) * 100:.2f}% ) ║
\033[0;33m ║  [ {progress_bar} ] {((atm + 1) / reff_limit) * 100:.2f}% ║
\033[1;35m ║  🔵 Status Message       : Referral In Progress        ║
\033[0;31m ║  🔴 Successful Referrals : {success_crt}/{reff_limit}  ║
\033[1;36m ╚═════════════════════════════════════════════════════════╝
""")

# Get proxy list
proxy_list = open('proxy.txt','r').read().splitlines()

# Get Captcha token
def get_token():
    while True:
        res = requests.get(f'http://localhost:5000/get').text
        if not 'None' in res:
            print(f'\r\r\033[0m>>\033[1;32m Captcha token get successful \033[0m')
            return res
        else:
            time.sleep(0.5)

# Register account using proxy
def reg_accaunt(email, password, username, ref_code, proxy_url=None, captcha_token=None):
    try:
        if proxy_url:
            print(f'\r\r\033[0m>>\033[1;32m Proxy : {proxy_url} \033[0m')
            proxy_url = {'http': proxy_url,'https': proxy_url}
        register_data = {
            'email': email,
            'password': password,
            'username': username,
            'referral_code': ref_code,
            'recaptcha_token': captcha_token
        }
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.nodepay.ai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }
        url = "https://api.nodepay.ai/api/auth/register"
        response = requests.post(url,headers=headers,json=register_data,proxies=proxy_url,timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')

# Main process for referral system
def main():
    clear_screen()
    try:
        reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:
        print('\033[1;32m⚠️ Input Wrong, Default Reff Amount is 1000');reff_limit=1000;time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen()
    success_crt = 0
    for atm in range(reff_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Processing: {atm + 1}/{reff_limit} complete: {((atm + 1) / reff_limit) * 100:.2f}%')
            display_progress(success_crt, reff_limit, atm)
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            if response_data['msg'] == 'Success':
                print(f'\r\r\033[0m>>\033[1;32m Account Create Successful \033[0m')
                captcha_token = get_token()
                response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
                if response_data['msg'] == 'Success':
                    success_crt += 1
                    print(f'\r\r\033[0m>>\033[1;32m Referral Done Successful \033[0m')
            else:
                print(f'\r\r\033[31m⚠️ Account Create Failed \033[0m {response_data["msg"]}')
            linex()
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')

    print('\r\r\033[0m>>\033[1;32m Your Referral Process is Complete \033[0m')
    exit()

# Call to start the program
if __name__ == "__main__":
    verify_password()  # Check the password first
    main()  # Proceed with the main function
