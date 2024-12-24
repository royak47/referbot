import os, sys, random, string, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests

# Line Function for modern style
def linex():
    print('\033[0m===============================================================')

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
\033[0m==============================================================
 \033[1;35m        Developer : Dark Life 🧬 
         Tele channel   : @scripthub00
         Tele group  : @scripthub0
\033[0m==============================================================
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
              print(f'\r\r\033[0m>>\033[1;32m Captcha token get successful 🌐\033[0m')
              return res
         else:
             time.sleep(0.5)

# clear terminal session & print logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls');print(logo)
    else:
        os.system('clear');print(logo)

# get ip using proxy
def get_ip(proxy_url):
     proxy = {'http': proxy_url,'https': proxy_url}
     try:
         response = requests.get('http://ip-api.com/json',proxies=proxy)
         return response.json()['query']
     except:
        return None

# get headers set with `auth_token`
def get_headers(auth_token=None):
     headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.nodepay.ai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
            }
     if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
            headers['origin'] = 'chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm'
     return headers

# Registration and login functions, same as in your code.

# Modern Output function to show messages in single chamber with different colors
def modern_output(message, color_code):
    color_map = {
        "green": '\033[1;32m',
        "red": '\033[1;31m',
        "blue": '\033[1;34m',
        "yellow": '\033[1;33m',
        "cyan": '\033[1;36m',
        "purple": '\033[1;35m',
    }
    
    print(f"\033[0m>> {color_map.get(color_code, '\033[1;37m')}{message}\033[0m")

# Example of the modern single chamber output with the process
def show_process_output():
    # Using chamber-style modern output for each process
    modern_output("Processing 2/10 completed: 70.00% 💻", "cyan")
    modern_output("Captcha token get successful 🌐", "green")
    modern_output("Proxy 🌍 : http://aqiddrde:wmxqhvx0p0j0@173.211.0.148:6641", "blue")
    modern_output("Account created successfully ✅", "green")
    modern_output("Captcha token get successful 🌐", "green")
    modern_output("Account logged in successfully ✅", "green")
    modern_output("Referral done successfully ✅", "yellow")

# Main logic to process the tasks
def main():
    clear_screen()
    try:
        reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:
        print('\033[1;32m⚠️ Input Wrong Default Reff Amaunt is 1k ')
        reff_limit = 1000
        time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen()
    success_crt = 0

    for atm in range(reff_limit):
        try:
            modern_output(f"Processing {str(success_crt)}/{str(reff_limit)} completed: {((atm + 1) / reff_limit) * 100:.2f}% 💻", "cyan")
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            if response_data['msg'] == 'Success':
                modern_output("Account created successfully ✅", "green")
                captcha_token = get_token()
                response_data = login_acccaunts(email, password, captcha_token, proxy_url)
                if response_data['msg'] == 'Success':
                    modern_output("Account logged in successfully ✅", "green")
                    auth_token = response_data['data']['token']
                    response_data = active_recent_accaunt(auth_token, proxy_url)
                    if response_data['msg'] == 'Success':
                        modern_output("Referral done successfully ✅", "yellow")
                        success_crt += 1
                        open('accaunts.txt', 'a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n")
                        time.sleep(1)
                    else:
                        modern_output(f"Referral Error: {response_data['msg']} 🌲", "red")
                        time.sleep(1)
                else:
                    modern_output(f"Login failed: {response_data['msg']} 🌲", "red")
                    time.sleep(1)
            else:
                modern_output(f"Account creation failed: {response_data['msg']} 🌲", "red")
                time.sleep(1)
            linex()
        except Exception as e:
            modern_output(f"⚠️ Error: {str(e)}", "red")
            linex()
            time.sleep(1)

    modern_output("Referral process completed ✅", "green")
    exit()

# Run the main process
main()
