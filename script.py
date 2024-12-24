import os, sys, random, string, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests

# Modern Line Function with unique look
def linex():
    print("\033[38;5;45m╔═══════════════════════════════════════════════════════╗\033[0m")

# Modern Logo with updated gradient colors
logo = f"""
\033[38;5;51m╔═══════════════════════════════════════════════════════╗
\033[38;5;159m║  \033[38;5;51m███████████████████████████████████████████  \033[0m  ║
\033[38;5;159m║  \033[38;5;51m██╔══██╗██╔══██╗██╔══██╗██████╗██╔══██╗  \033[0m  ║
\033[38;5;159m║  \033[38;5;51m████████║███████║██████╔╝███████║███████║  \033[0m  ║
\033[38;5;159m║  \033[38;5;51m██╔══██║██╔══██║██╔══██╗██╔══██║██╔══██║  \033[0m  ║
\033[38;5;159m║  \033[38;5;51m██║  ██║██║  ██║██║  ██║██████╔╝██║  ██║  \033[0m  ║
\033[38;5;159m║  \033[38;5;51m╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝  \033[0m  ║
\033[38;5;159m╚═══════════════════════════════════════════════════════╝
\033[1;35m        Developer : Dark Life 🧬
        Tele channel   : @scripthub00
        Tele group  : @scripthub0
\033[0m
"""

# Display the updated logo
linex()
print(logo)
linex()

# Password Protection Function
def verify_password():
    correct_password = "darkwithX"
    print("\033[0m🛡️ \033[1;32mEnter the password to access this script: \033[0m", end="")
    entered_password = input()
    if entered_password != correct_password:
        print("\033[1;31m⚠️ Incorrect password! Exiting...\033[0m")
        sys.exit()
    else:
        print("\033[1;32m🔓 Password correct! Proceeding...\033[0m")
        time.sleep(1)

# Prompt for password before proceeding
verify_password()

proxy_list = open('proxy.txt', 'r').read().splitlines()

# Get Captcha token
def get_token():
    while True:
        res = requests.get(f'http://localhost:5000/get').text
        if not 'None' in res:
            print(f'\r\r\033[0m🧩 \033[1;32mCaptcha token fetched successfully! \033[0m')
            return res
        else:
            time.sleep(0.5)

# Get IP using proxy (not using for speed up)
def get_ip(proxy_url):
    proxy = {'http': proxy_url, 'https': proxy_url}
    try:
        response = requests.get('http://ip-api.com/json', proxies=proxy)
        return response.json()['query']
    except:
        return None

# Get headers with or without `auth_token`
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

# Active account and confirmation
def active_recent_account(auth_token, proxy_url):
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
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m'); linex(); time.sleep(1)

# Main function for full action with unique colors and emojis
def main():
    clear_screen()
    try:
        reff_limit = int(input('\033[0m💡 \033[1;32mEnter your referral amount: '))
    except:
        print('\033[1;32m⚠️ Input wrong! Default referral amount is 1000.\033[0m')
        reff_limit = 1000
        time.sleep(1)
    
    ref_code = input("\033[0m💬 \033[1;32mInput referral code: ")
    clear_screen()
    success_crt = 0
    for atm in range(reff_limit):
        try:
            print(f'\r\r\033[0m⏳ \033[1;32mProcessing referral {str(success_crt)}/{str(reff_limit)} complete: {((atm+1) / reff_limit) * 100:.2f}%')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            if response_data['msg'] == 'Success':
                print(f'\r\r\033[0m✅ \033[1;32mAccount created successfully! \033[0m')
                captcha_token = get_token()
                response_data = login_acccaunts(email, password, captcha_token, proxy_url)
                if response_data['msg'] == 'Success':
                    print(f'\r\r\033[0m✅ \033[1;32mAccount login successful! \033[0m')
                    auth_token = response_data['data']['token']
                    response_data = active_recent_account(auth_token, proxy_url)
                    if response_data['msg'] == 'Success':
                        print(f'\r\r\033[0m🎉 \033[1;32mReferral successfully completed! \033[0m')
                        success_crt += 1
                        open('accounts.txt', 'a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n")
                        time.sleep(1)
                    else:
                        print(f'\r\r\033[1;31m⚠️ Referral Error: {response_data["msg"]} \033[0m')
                        time.sleep(1)
                else:
                    print(f'\r\r\033[1;31m⚠️ Account login failed: {response_data["msg"]} \033[0m')
                    time.sleep(1)
            else:
                print(f'\r\r\033[1;31m⚠️ Account creation failed: {response_data["msg"]} \033[0m')
                time.sleep(1)
            linex()
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
            linex()
            time.sleep(1)
    print('\r\r\033[0m🎉 \033[1;32mYour referral process is completed!\033[0m')
    exit()

# Call main function to execute the script
main()
