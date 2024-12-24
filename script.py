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

# Fetch proxy list
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

# clear terminal session & print logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls');print(logo)
    else:
        os.system('clear');print(logo)

# Get IP using proxy (not used for speed-up)
def get_ip(proxy_url):
    proxy = {'http': proxy_url, 'https': proxy_url}
    try:
        response = requests.get('http://ip-api.com/json', proxies=proxy)
        return response.json()['query']
    except:
        return None

# Get headers for requests
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

# Register account
def reg_accaunt(email, password, username, ref_code, proxy_url=None, captcha_token=None):
    try:
        if proxy_url:
            print(f'\r\r\033[0m>>\033[1;32m Proxy : {proxy_url} \033[0m')
            proxy_url = {'http': proxy_url, 'https': proxy_url}
        register_data = {
            'email': email,
            'password': password,
            'username': username,
            'referral_code': ref_code,
            'recaptcha_token': captcha_token
        }
        headers = get_headers()
        url = "https://api.nodepay.ai/api/auth/register"
        response = requests.post(url, headers=headers, json=register_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Login account and fetch authorization token
def login_acccaunts(email, password, captcha_token, proxy_url):
    try:
        json_data = {
            'user': email,
            'password': password,
            'remember_me': True,
            'recaptcha_token': captcha_token
        }
        proxy_url = {'http': proxy_url, 'https': proxy_url}
        headers = get_headers()
        url = "https://api.nodepay.ai/api/auth/login"
        response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Activate account
def active_recent_accaunt(auth_token, proxy_url):
    try:
        json_data = {}
        url = "https://api.nodepay.ai/api/auth/active-account"
        headers = get_headers(auth_token)
        proxy_url = {'http': proxy_url, 'https': proxy_url}
        response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        if not response.json()['msg'] == 'Success':
            response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        if not response.json()['msg'] == 'Success':
            response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Chamber Progress Display
def chamber_display(success_crt, atm, reff_limit, status, detail=None):
    progress = int(((atm + 1) / reff_limit) * 100)
    progress_bar = f"[{'#' * (progress // 2)}{' ' * (50 - (progress // 2))}] {progress}%"
    status_color = "\033[1;32m" if status == "Referral Successfully Done" else "\033[1;33m"
    error_color = "\033[1;31m" if status != "Referral Successfully Done" else ""

    linex()
    print(f"""
\033[0;36m╔═════════════════════════════════════════════════════════╗
\033[0;32m║\033[1;33m      🔰 Referral Progress Dashboard 🔰       \033[0;32m║
\033[0;36m╠═════════════════════════════════════════════════════════╣
\033[1;32m║  ✅ Successful Referrals  : \033[0;32m{success_crt}/{reff_limit}  \033[1;32m║
\033[1;33m║  🟢 Current Progress      : \033[0;33m{atm+1}/{reff_limit} \033[0;36m({((atm+1) / reff_limit) * 100:.2f}% )\033[0;36m ║
\033[1;33m║  {progress_bar}                                       ║
\033[0;34m║  🔵 Status Message        : \033[0;34m{status_color}{status}\033[0m      ║
\033[0;31m║  🔴 Detail                : \033[1;31m{detail if detail else 'N/A'}\033[0m       ║
\033[0;36m╠═════════════════════════════════════════════════════════╣
\033[1;33m║  🚀 Keep Going... Your progress is on track!         ║
\033[0;36m╚═════════════════════════════════════════════════════════╝
""")
    linex()

# Main function
def main():
    clear_screen()
    try:
        reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except ValueError:
        print('\033[1;32m⚠️ Input is invalid. Defaulting reff amount to 1000.\033[0m')
        reff_limit = 1000
        time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen()
    success_crt = 0
    for atm in range(reff_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Processing: {str(success_crt)}/{str(reff_limit)} complete: {((atm+1) / reff_limit) * 100:.2f}% ')
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
                response_data = login_acccaunts(email, password, captcha_token, proxy_url)
                if response_data['msg'] == 'Success':
                    print(f'\r\r\033[0m>>\033[1;32m Account Login Successfuly \033[0m')
                    auth_token = response_data['data']['token']
                    response_data = active_recent_accaunt(auth_token, proxy_url)
                    if response_data['msg'] == 'Success':
                         print(f'\r\r\033[0m>>\033[1;32m Successful Referral Done \033[0m')
                         success_crt += 1
                         open('accaunts.txt', 'a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n")
                         chamber_display(success_crt, atm, reff_limit, "Referral Successfully Done")
                         time.sleep(1)
                    else:
                        print(f'\r\r\033[1;31m🌲 Referral Error, Not Success \033[0m {response_data["msg"]}')
                        time.sleep(1)
                        linex()
                else:
                    print(f'\r\r\033[1;31m🌲 Account Login Failed \033[0m {response_data["msg"]}')
                    time.sleep(1)
                    linex()
            else:
                print(f'\r\r\033[1;31m🌲 Account Create Failed \033[0m {response_data["msg"]}')
                time.sleep(1)
                linex()
            linex()
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
            linex()
            time.sleep(1)

# Start the program
main()
