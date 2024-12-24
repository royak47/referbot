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

# Chamber Box Function
def chamber_box(message, box_color="38;5;82", text_color="1;32"):
    print(f"\033[0m\x1b[{box_color}m╔════════════════════════════════════════════════════════╗\033[0m")
    print(f"\033[0m\x1b[{box_color}m║\033[1;37m {message} \033[0m\x1b[{box_color}m║\033[0m")
    print(f"\033[0m\x1b[{box_color}m╚════════════════════════════════════════════════════════╝\033[0m")
    time.sleep(1)

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
       chamber_box(f"⚠️ Error: {str(e)}", box_color="38;5;196", text_color="1;31"); time.sleep(1)

# login account and age authorization token
def login_acccaunts(email, password, captcha_token, proxy_url):
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
       chamber_box(f"⚠️ Error: {str(e)}", box_color="38;5;196", text_color="1;31"); time.sleep(1)

# active account and confirmation 
def active_recent_accaunt(auth_token, proxy_url):
   try:
       json_data = {}
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
       chamber_box(f"⚠️ Error: {str(e)}", box_color="38;5;196", text_color="1;31"); time.sleep(1)

# main def for possess full action
def main():
    clear_screen()
    try:
        reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:
        chamber_box("⚠️ Input Wrong, Default Reff Amount is 1k", box_color="38;5;196", text_color="1;31")
        reff_limit = 1000; time.sleep(1)
    
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen(); success_crt = 0
    
    for atm in range(reff_limit):
        try:
            chamber_box(f"Possessing {str(success_crt)}/{str(reff_limit)} complete : {((atm+1) / reff_limit) * 100:.2f}%", box_color="38;5;214", text_color="1;33")
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            
            chamber_box(f"Proxy : {proxy_url}", box_color="38;5;208", text_color="1;37")
            captcha_token = get_token()
            chamber_box(f"Captcha token get successful", box_color="38;5;82", text_color="1;32")
            
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            
            if response_data['msg'] == 'Success':
                chamber_box("Account Create Successful", box_color="38;5;82", text_color="1;32")
                captcha_token = get_token()
                response_data = login_acccaunts(email, password, captcha_token, proxy_url)
                
                if response_data['msg'] == 'Success':
                    chamber_box("Account Login Successfully", box_color="38;5;82", text_color="1;32")
                    auth_token = response_data['data']['token']
                    response_data = active_recent_accaunt(auth_token, proxy_url)
                    
                    if response_data['msg'] == 'Success':
                         chamber_box("Successfully Referral Done", box_color="38;5;82", text_color="1;32")
                         success_crt += 1
                         open('accaunts.txt','a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n"); time.sleep(1)
                    else:
                        chamber_box(f"Referral Error, Not Success: {response_data['msg']}", box_color="38;5;196", text_color="1;31")
                        time.sleep(1)
                else:
                    chamber_box(f"Account Login Failed: {response_data['msg']}", box_color="38;5;196", text_color="1;31")
                    time.sleep(1)
            else:
                chamber_box(f"Account Create Failed: {response_data['msg']}", box_color="38;5;196", text_color="1;31")
                time.sleep(1)

            linex()
        except Exception as e:
            chamber_box(f"⚠️ Error: {str(e)}", box_color="38;5;196", text_color="1;31")
            linex(); time.sleep(1)
    
    chamber_box("Your Referral Completed", box_color="38;5;82", text_color="1;32")
    exit()

main()
