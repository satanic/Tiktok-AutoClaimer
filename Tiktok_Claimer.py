import requests
import os
import sys
import time
from itertools import cycle
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from random import randint, choice
from Data.UserAgent import UserAgent
from threading import active_count, Thread

proxiesloaded = False
proxies = []
proxy = []
endmsg = False
os.system("title Tiktok AutoClaimer By aac#3444 ¦ github.com/jgord559")
r = requests.session()

requestcount = 0
failcount = 0

###proxies###
def load_proxies():
    global filename
    if not os.path.exists(filename):
        print("File Error")
        time.sleep(10)
        sys.exit()
    with open(filename, "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
            proxiesloaded = True
        if not len(proxies):
            print("No proxies in file")
            time.sleep(10)
            sys.exit()

option = int(input("[1] Proxies \ [2] Proxyless: "))
if option == 1:
    if os.name == 'nt':
        print("Please select your proxies file")
        Tk().withdraw()
        filename = askopenfilename()
        #print(filename)
    else:
        filename = input("Please enter where your proxies are stored. (eg etc/home/proxies.txt): ")
    load_proxies()
###

# "login_name={user}"
###getting checker cookies###
#checkcookiehed = {
#'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
#checkcookiereq = requests.get(f"https://www.tiktok.com/@{user}", headers=checkcookiehed)
#print(checkcookiereq.cookies['ttwid'])
#mstok = (checkcookiereq.cookies['ttwid'])

r = requests.session()
user = input("Please enter the user to claim: ")
checksid = input("Please enter the sessionid of the account you want to check avalibility: ")
sid = input("Please enter the sessionid of the account you want to claim to: ")
tttokenreq = requests.get("https://tiktok.com/signup", headers={'cookie': f'sessionid={sid}'})
tttoken = (tttokenreq.cookies['tt_csrf_token'])
#print(tttoken)
threadcount = int(input("Please enter the ammount of threads to use: "))

###NO PROXYS USES ON CLAIM###

def check():
    global proxies
    global proxy
    global requestcount
    global failcount
    while True:
        os.system("title Tiktok AutoClaimer By aac#3444 ¦ github.com/jgord559 ¦ Requests Sent: " + str(requestcount) + " " + str(failcount))
        deviceid = randint(1000000000000000000, 9999999999999999999)
        useragent = choice(UserAgent)
        checkurl = (f"https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&battery_info=1&browser_online=true&channel=tiktok_web&device_id={deviceid}&device_platform=web_pc&uniqueId={user}")
        checkhed = {
            'user-agent': 'fdsa',
            'cookie': f'sessionid={checksid}',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}   
        checkreq = requests.get(checkurl, headers=checkhed)

        if '"statusCode":10202' in (checkreq.text):
            requestcount += 1
            print("[+] " + "@" + user + " is avalible!")
            claim()

        if '"statusCode":0' in (checkreq.text):
            requestcount += 1
            print("[-] " + "@" + user + " is taken")

        if '"statusCode":10221' in (checkreq.text):
            requestcount += 1
            print("[-] " + "@" + user + " is banned")
        else:
            failcount += 1


###CLAIMPROXY USES PROXYS###

def checkproxy():
    global proxies
    global proxy
    global requestcount
    global failcount
    while True:
        os.system("title Tiktok AutoClaimer By aac#3444 ¦ github.com/jgord559 ¦ Requests Sent: " + str(requestcount) + " " + str(failcount))
        deviceid = randint(1000000000000000000, 9999999999999999999)
        useragent = choice(UserAgent)
        checkurl = (f"https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&battery_info=1&browser_online=true&channel=tiktok_web&device_id={deviceid}&device_platform=web_pc&uniqueId={user}")
        checkhed = {
            'user-agent': 'fdsa',
            'cookie': f'sessionid={checksid}',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}   
        checkreq = requests.get(checkurl, headers=checkhed, proxies={"http": proxy})

        if '"statusCode":10202' in (checkreq.text):
            requestcount += 1
            print("[+] " + "@" + user + " is avalible!")
            claim()

        if '"statusCode":0' in (checkreq.text):
            requestcount += 1
            print("[-] " + "@" + user + " is taken")

        if '"statusCode":10221' in (checkreq.text):
            requestcount += 1
            print("[-] " + "@" + user + " is banned")
        else:
            failcount += 1

###claim req###

def claim():
    global user
    global tttoken
    global sid
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


if option == 1:
    for x in range(threadcount):
        Thread(target=(checkproxy)).start()
        time.sleep(0.2)
else:
    for x in range(threadcount):
        Thread(target=(check)).start()
        time.sleep(0.2)
