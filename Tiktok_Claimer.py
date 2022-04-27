import requests
import os
import sys
import time
from random import randint, choice
from Data.UserAgent import UserAgent
from threading import active_count, Thread

endmsg = False
os.system("title Tiktok AutoClaimer By aac#3444 ¦ github.com/jgord559")
r = requests.session()

requestcount = 0

###getting checker cookies###
#checkcookiereq = requests.get("https://www.tiktok.com/")
#print(checkcookiereq.cookies['msToken'])
#mstok = (checkcookiereq.cookies['msToken'])


user = input("Please enter the user to claim: ")
checksid = input("Please enter the sessionid of the account you want to check avalibility: ")
sid = input("Please enter the sessionid of the account you want to claim to: ")
tttokenreq = requests.get("https://tiktok.com/signup", headers={'cookie': f'sessionid={sid}'})
tttoken = (tttokenreq.cookies['tt_csrf_token'])
threadcount = int(input("Please enter the ammount of threads to use: "))

r = requests.session()


def claim():
    global requestcount
    while True:
        os.system("title Tiktok AutoClaimer By aac#3444 ¦ github.com/jgord559 ¦ Requests Sent: " + str(requestcount))
        deviceid = randint(1000000000000000000, 9999999999999999999)
        useragent = choice(UserAgent)
        checkurl = (f"https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&battery_info=1&browser_online=true&channel=tiktok_web&device_id={deviceid}&device_platform=web_pc&uniqueId={user}")
        checkhed = {
            'user-agent': 'fdsa',
            'cookie': f'sessionid={checksid}',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        checkreq = requests.get(checkurl, headers=checkhed)
        requestcount += 1

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
                if endmsg == True:
                    pass
                else:
                    endmsg = True
                    print("Claimed " + user + " Successfully!")
                    input("Click enter to exit")
                    sys.exit()
            else:
                pass
                sys.exit()

        if '"statusCode":0' in (checkreq.text):
            print("[-] " + "@" + user + " is taken")

        if '"statusCode":10221' in (checkreq.text):
            print("[-] " + "@" + user + " is banned")
       #else:
            #print("[-] Request Failed")


for x in range(threadcount):
    Thread(target=(claim)).start()
    time.sleep(0.2)
