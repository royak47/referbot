import os, sys, random, string, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests

# Line Function 
def linex():
    print('\033[0m================================================')

# Logo for script with gradient colors
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
linex()
print(logo)
linex()

# Password Protection
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

# Prompt for password before proceeding
verify_password()

proxy_list = open('proxy.txt', 'r').read().splitlines()

# get Captcha token 
def get_token():
    while True:
         res = requests.get(f'http://localhost:5000/get').text
         if not 'None' in res:
              print(f'\033[0m>>\033[1;32m Captcha token get successful \033[0m')
              return res
         else:
             time.sleep(0.5)

# clear terminal session & print logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls');print(logo)
    else:
        os.system('clear');print(logo)

# Display chambered logs
def display_chamber(logs, success_crt, reff_limit):
    print("\033[38;5;51m╭──────────────────────────────────────────╮\033[0m")
    print(f"\033[38;5;154m│ Referral {success_crt}/{reff_limit} ({(success_crt/reff_limit)*100:.2f}%)\033[0m")
    for log in logs:
        print(f"\033[38;5;51m│ {log}\033[0m")
    print("\033[38;5;51m╰──────────────────────────────────────────╯\033[0m")

# main def for possess full action
def main():
    clear_screen()
    try: 
        reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except: 
        print('\033[1;32m⚠️ Input Wrong Default Reff Amount is 1k '); reff_limit = 1000; time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen(); success_crt = 0
    for atm in range(reff_limit):
        logs = []  # To collect logs for this referral process
        try:
            print(f'\r\r\033[0m>>\033[1;32m Processing  {str(success_crt)}/{str(reff_limit)} complete : {((atm+1) / reff_limit) * 100:.2f}% ')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = ''.join(random.choice(characters) for _ in range(12)).lower()
            password = ''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3))
            email = f"{username}{random.choice(domains)}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            
            # Register account
            logs.append(f"\033[38;5;118m>> Account Created Successfully!\033[0m")
            response_data = {"msg": "Success"}  # Mocking success for demonstration
            
            # Login account
            if response_data["msg"] == "Success":
                logs.append(f"\033[38;5;213m>> Account Logged In Successfully!\033[0m")
                auth_token = "mock_auth_token"  # Mocking auth token for demonstration
                
                # Active account
                response_data = {"msg": "Success"}  # Mocking success for demonstration
                if response_data["msg"] == "Success":
                    logs.append(f"\033[38;5;82m>> Referral Successful!\033[0m")
                    success_crt += 1
                    open('accounts.txt', 'a').write(f"{email}|{password}|{auth_token}\n")
                else:
                    logs.append(f"\033[38;5;196m>> Referral Error: {response_data['msg']}\033[0m")
            else:
                logs.append(f"\033[38;5;196m>> Account Login Failed: {response_data['msg']}\033[0m")
            
            # Display chamber
            display_chamber(logs, success_crt, reff_limit)
            time.sleep(1)
        
        except Exception as e:
            logs.append(f"\033[31m⚠️ Error: {str(e)} \033[0m")
            display_chamber(logs, success_crt, reff_limit)
            time.sleep(1)
    print('\r\r\033[0m>>\033[1;32m Your Referral Completed \033[0m')
    exit()

main()
