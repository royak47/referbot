import os, sys, random, string, time
try:
    import requests
except:
    os.system('pip install requests')
    import requests

# Line Function 
def linex():
    print('\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')

# "DARK" in ASCII art with gradient colors
dark_logo = f"""
\033[38;5;45m -================= ≫ ──── ≪•◦ ❈ ◦•≫ ──── ≪=================-
\033[38;5;51m │                                                          │
\033[38;5;87m │  ██████╗  █████╗ ██████╗ ██╗  ██╗                        │
\033[38;5;123m │  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝                        │
 \033[38;5;159m│  ██║  ██║███████║██████╔╝█████╔╝                         │
\033[38;5;159m │  ██║  ██║██╔══██║██╔══██╗██╔═██╗                         │
\033[38;5;195m │  ██████╔╝██║  ██║██║  ██║██║  ██╗                        │
\033[38;5;51m │  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                        │
\033[38;5;87m │                                                          │
\033[38;5;123m │                                                          │
 \033[38;5;123m╰─━━━━━━━━━━━━━━━━━━━━━━━━Termux-os━━━━━━━━━━━━━━━━━━━━━━━─╯
"""

# Full logo with additional details
logo_details = f"""
\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[38;5;39m          Developer   : \033[38;5;207mDark Life 🧬
\033[38;5;39m          Telegram    : \033[38;5;199m@scripthub00
\033[38;5;39m          Group       : \033[38;5;163m@scripthub0
\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Display the logo
linex()
print(dark_logo)
print(logo_details)
linex()
# Password Protection
def verify_password():
    correct_password = "darkwithX"
    # Dark Sky Blue ANSI code is \033[38;5;32m or using \033[48;5;32m for background
    print("\033[38;5;32m>>\033[1;44m Enter the password to access this script: \033[0m", end="")
    entered_password = input()
    if entered_password != correct_password:
        print("\033[38;5;32m⚠️ Incorrect password! Exiting...\033[0m")
        sys.exit()
    else:
        print("\033[38;5;32m>> Password correct! Proceeding...\033[0m")
        time.sleep(1)

# Prompt for password before proceeding
verify_password()

proxy_list = open('proxy.txt','r').read().splitlines()

# get Captcha token 
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
        os.system('cls'); print(dark_logo)  # Use dark_logo or the logo you want
    else:
        os.system('clear'); print(dark_logo)  # Use dark_logo or the logo you want

def chamber_display(success_crt, atm, reff_limit, status, detail=None):
    linex()
    print(f"""
\033[1;35m ╔═══════════════════════════════════════════════════════╗
\033[1;35m ║                Referrals Progress            
\033[1;35m ║  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   
\033[1;35m ║                                                     
\033[0;32m ║   ✅ Successful Referrals    : {success_crt}/{reff_limit}             
\033[0;33m ║   🟢 Current Progress        : {atm+1}/{reff_limit} ({((atm+1) / reff_limit) * 100:.2f}%)      
\033[0;34m ║   🔵 Status Message          : {status}                              
\033[0;31m ║   🔴 Detail                  : {detail if detail else 'N/A'}                
\033[1;35m ║                                                     
\033[1;36m ║----------------------------------------------------->
\033[1;35m ║                  End of Progress          
\033[1;35m ╚═══════════════════════════════════════════════════════╝
""")
    linex()

# get ip using proxy  / not using for speed up
def get_ip(proxy_url):
     proxy = {'http': proxy_url,'https': proxy_url}
     try:
         response = requests.get('http://ip-api.com/json',proxies=proxy)
         return response.json()['query']
     except:
        return None

# get headers set / with `auth_token` or head only
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

# registration account  |  using proxy or not
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
       headers = get_headers()
       url = "https://api.nodepay.ai/api/auth/register"
       response = requests.post(url,headers=headers,json=register_data,proxies=proxy_url,timeout=5)
       response.raise_for_status()
       return response.json()
   except Exception as e:
       print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)

# login account and age authorization token
def login_acccaunts(email, password, captcha_token,proxy_url):
   try:
       json_data = {
           'user': email,
           'password': password,
           'remember_me': True,
           'recaptcha_token': captcha_token
       }
       proxy_url = {'http': proxy_url,'https': proxy_url}
       headers = get_headers()
       url = "https://api.nodepay.ai/api/auth/login"
       response = requests.post(url,headers=headers,json=json_data,proxies=proxy_url,timeout=5)
       response.raise_for_status()
       return response.json()
   except Exception as e:
       print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)

# active account and confirmation 
def active_recent_accaunt(auth_token,proxy_url):
   try:
       json_data={}
       url = "https://api.nodepay.ai/api/auth/active-account"
       headers = get_headers(auth_token)
       proxy_url = {'http': proxy_url,'https': proxy_url}
       response = requests.post(url, headers=headers,json=json_data,proxies=proxy_url,timeout=5)
       response.raise_for_status()
       if not response.json()['msg'] == 'Success':
           response = requests.post(url, headers=headers,json=json_data,proxies=proxy_url,timeout=5)
       if not response.json()['msg'] == 'Success':
           response = requests.post(url, headers=headers,json=json_data,proxies=proxy_url,timeout=5)
       return response.json()
   except Exception as e:
       print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)

# main def for possess full action
def main():
    clear_screen()
    try:reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:print('\033[1;32m⚠️ Input Wrong Default Reff Amount is 1k ');reff_limit=1000;time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen();success_crt = 0
    for atm in range(reff_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Possessing  {str(success_crt)}/{str(reff_limit)} complete : {((atm+1) / reff_limit) * 100:.2f}% ')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            if response_data['msg'] == 'Success':
                status = "Account Created Successfully"
                chamber_display(success_crt, atm, reff_limit, status)
                captcha_token = get_token()
                response_data = login_acccaunts(email, password, captcha_token,proxy_url)
                if response_data['msg'] == 'Success':
                    status = "Account Logged In Successfully"
                    chamber_display(success_crt, atm, reff_limit, status)
                    auth_token = response_data['data']['token']
                    response_data = active_recent_accaunt(auth_token,proxy_url)
                    if response_data['msg'] == 'Success':
                         status = "Referral Successfully Done"
                         success_crt+=1
                         chamber_display(success_crt, atm, reff_limit, status)
                         open('accaunts.txt','a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n");time.sleep(1)
                    else:
                        status = "Referral Error, Not Success"
                        chamber_display(success_crt, atm, reff_limit, status, response_data["msg"])
                else:
                    status = "Account Login Failed"
                    chamber_display(success_crt, atm, reff_limit, status, response_data["msg"])
            else:
                status = "Account Creation Failed"
                chamber_display(success_crt, atm, reff_limit, status, response_data["msg"])

        except Exception as e:
            status = "Error"
            chamber_display(success_crt, atm, reff_limit, status, str(e))

    print('\033[0m>>\033[1;32m Your Referral Completed \033[0m')
    exit()

# Run main function
main()
