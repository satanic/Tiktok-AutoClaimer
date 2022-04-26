import requests
import sys
from random import randint, choice
from Data.UserAgent import UserAgent
import threading


user = input("Please enter the user to claim: ")
checksid = input("Please enter the sessionid of the account you want to check avalibility: ")
sid = input("Please enter the sessionid of the account you want to claim to: ")
tttoken = input("Please enter the tt_csrf_token of the account you want to claim to: ")

r = requests.session()

def claim():
    while True:
        deviceid = randint(1000000000000000000, 9999999999999999999)
        useragent = choice(UserAgent)
        checkurl = (f"https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&battery_info=1&browser_online=true&channel=tiktok_web&device_id={deviceid}&device_platform=web_pc&uniqueId={user}")
        checkhed = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'cookie': f'sessionid={checksid}',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        checkreq = requests.get(checkurl, headers=checkhed)

        if '"statusCode":10202' in (checkreq.text):
            print("[+] " + "@" + user + " is avalible!")
            claimurl = ("https://www.tiktok.com/passport/web/login_name/update/?aid=1988&app_name=tiktok_web&battery_info=1&browser_online=true&channel=tiktok_web&cookie_enabled=true&device_id=7090239850439493126&device_platform=web_pc")
            claimhed = {
                'Host': 'www.tiktok.com',
                'Connection': 'close',
                'Content-Length': '102',
                'tt-csrf-token': f'{tttoken}',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.tiktok.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': f'https://www.tiktok.com/@{user}',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Cookie': f'sessionid={sid};'}
            claimreq = requests.post(claimurl, headers=claimhed, data=f"login_name={user}")
            #print(claimreq.text)
            if '"message":success' in (claimreq.text):
                print("Claimed " + user + " Successfully!")
                input("Click enter to exit")
                sys.exit()
            else:
                print("Error occured when attemting to claim.")
                input("Click enter to exit")
                sys.exit()

        if '"statusCode":0' in (checkreq.text):
            print("[-] " + "@" + user + " is taken")

        if '"statusCode":10221' in (checkreq.text):
            print("[-] " + "@" + user + " is banned")
       #else:
            #print("[-] Request Failed")


#claim()

t1 = threading.Thread(target=claim)
t2 = threading.Thread(target=claim)
t3 = threading.Thread(target=claim)
t4 = threading.Thread(target=claim)


t1.start()
t2.start()
t3.start()
t4.start()
















