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

proxy_list = open('proxy.txt','r').read().splitlines()

# get Captcha token 
def get_token():
    while True:
         res = requests.get(f'http://localhost:5000/get').text
         if not 'None' in res:
              print(f'\033[38;5;118m>> Captcha token get successful \033[0m')  # Light Green for success
              return res
         else:
             time.sleep(0.5)

# clear terminal session & print logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls');print(logo)
    else:
        os.system('clear');print(logo)

# Main function to process referrals
def main():
    clear_screen()
    try: 
        reff_limit = int(input('\033[38;5;118m>> Put Your Referral Amount: \033[0m'))
    except:
        print('\033[38;5;214m⚠️ Input wrong, default referral amount is 1k \033[0m')
        reff_limit = 1000
        time.sleep(1)

    ref_code = input("\033[38;5;118m>> Input referral code: \033[0m")
    clear_screen()
    success_crt = 0

    for atm in range(reff_limit):
        try:
            print(f'\r\033[38;5;220m>> Processing {str(success_crt)}/{str(reff_limit)} complete: {((atm+1) / reff_limit) * 100:.2f}% \033[0m', end="")
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = ''.join(random.choice(characters) for _ in range(12)).lower()
            password = ''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3))
            email = f"{username}{random.choice(domains)}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            print(f'\033[38;5;202m>> Proxy: {proxy_url} \033[0m')  # Orange for proxy display
            
            # Registration and further processes
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            if response_data['msg'] == 'Success':
                print(f'\033[38;5;118m>> Account Create Successful \033[0m')  # Light Green
                captcha_token = get_token()
                response_data = login_acccaunts(email, password, captcha_token, proxy_url)
                if response_data['msg'] == 'Success':
                    print(f'\033[38;5;82m>> Account Login Successfully \033[0m')  # Dark Green
                    auth_token = response_data['data']['token']
                    response_data = active_recent_accaunt(auth_token, proxy_url)
                    if response_data['msg'] == 'Success':
                        print(f'\033[38;5;226m>> Successfully Referral Done \033[0m')  # Yellow
                        success_crt += 1
                        open('accounts.txt', 'a').write(f"{email}|{password}|{auth_token}\n")
                        time.sleep(1)
                    else:
                        print(f'\033[38;5;196m>> Referral Error: {response_data["msg"]} \033[0m')  # Red
                        linex()
                else:
                    print(f'\033[38;5;196m>> Account Login Failed: {response_data["msg"]} \033[0m')  # Red
                    linex()
            else:
                print(f'\033[38;5;196m>> Account Creation Failed: {response_data["msg"]} \033[0m')  # Red
                linex()
            linex()
        except Exception as e:
            print(f'\033[38;5;196m⚠️ Error: {str(e)} \033[0m')  # Red for exceptions
            linex()
            time.sleep(1)

    print(f'\033[38;5;118m>> Referral Process Completed \033[0m')  # Light Green
    exit()

main()
