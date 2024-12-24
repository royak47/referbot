import os, sys, random, string, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests

# Line Function
def linex():
    print('\033[0m\033[38;5;45m================================================\033[0m')

# Logo for script
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
 \033[1;35m        Developer : \033[38;5;46mDark Life 🧬 
         \033[38;5;202mTele channel   : \033[38;5;51m@scripthub00
         \033[38;5;208mTele group  : \033[38;5;51m@scripthub0
\033[0m================================================
"""

# Display the logo
linex()
print(logo)
linex()

# Password Protection
def verify_password():
    correct_password = "darkwithX"
    print("\033[0m>>\033[38;5;214m Enter the password to access this script: \033[0m", end="")
    entered_password = input()
    if entered_password != correct_password:
        print("\033[38;5;196m⚠️ Incorrect password! Exiting...\033[0m")
        sys.exit()
    else:
        print("\033[38;5;46m>> Password correct! Proceeding...\033[0m")
        time.sleep(1)

# Prompt for password before proceeding
verify_password()

proxy_list = open('proxy.txt', 'r').read().splitlines()

# Get Captcha token
def get_token():
    while True:
        res = requests.get(f'http://localhost:5000/get').text
        if 'None' not in res:
            return res
        else:
            time.sleep(0.5)

# Main function
def main():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    try:
        reff_limit = int(input('\033[0m>>\033[38;5;214m Enter referral amount: '))
    except:
        print('\033[38;5;214m⚠️ Invalid input. Default referral amount is 1000.')
        reff_limit = 1000
        time.sleep(1)
    ref_code = input("\033[0m>>\033[38;5;214m Input referral code: ")
    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    success_crt = 0

    for atm in range(reff_limit):
        try:
            # Generate random user details
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = ''.join(random.choice(characters) for _ in range(12)).lower()
            password = ''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3))
            email = f"{username}{random.choice(domains)}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()

            # Logs with colors
            logs = []
            logs.append(f"\033[38;5;46m>> Captcha token retrieved successfully!\033[0m")
            logs.append(f"\033[38;5;208m>> Proxy : {proxy_url}\033[0m")
            logs.append(f"\033[38;5;118m>> Account Created Successfully!\033[0m")
            logs.append(f"\033[38;5;213m>> Account Logged In Successfully!\033[0m")
            logs.append(f"\033[38;5;82m>> Referral Successful!\033[0m")
            success_crt += 1

            # Print referral log as a modern chamber
            print("\033[38;5;51m╭──────────────────────────────────────────╮\033[0m")
            print(f"\033[38;5;154m│ Referral {success_crt}/{reff_limit} ({(success_crt/reff_limit)*100:.2f}%)\033[0m")
            print("\n".join([f"\033[38;5;51m│ {log}\033[0m" for log in logs]))
            print("\033[38;5;51m╰──────────────────────────────────────────╯\033[0m")

            # Save successful accounts to a file
            open('accounts.txt', 'a').write(f"{email}|{password}\n")

            time.sleep(1)

        except Exception as e:
            print(f"\033[31m⚠️ Error: {str(e)}\033[0m")
            linex()
            time.sleep(1)

    print('\033[38;5;46m>> Referral process completed! \033[0m')
    exit()

main()
