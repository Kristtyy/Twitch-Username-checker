import os
import requests, random, threading
from colorama import Fore


def check():
    os.system('cls')
    while True:
        with open('Available.txt', 'a') as f:
            user = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4))
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.7',
                'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                'Client-Integrity': 'v4.public.eyJjbGllbnRfaWQiOiJraW1uZTc4a3gzbmN4NmJyZ280bXY2d2tpNWgxa28iLCJjbGllbnRfaXAiOiIyMTMuMTE4LjIxNi4yMTYiLCJkZXZpY2VfaWQiOiJESUtTSUZXZGhCVG1pdnVwWWRVdlNnOElXeVFwQ0ZJVSIsImV4cCI6IjIwMjItMTItMDRUMDU6MDY6NDVaIiwiaWF0IjoiMjAyMi0xMi0wM1QxMzowNjo0NVoiLCJpc19iYWRfYm90IjoiZmFsc2UiLCJpc3MiOiJUd2l0Y2ggQ2xpZW50IEludGVncml0eSIsIm5iZiI6IjIwMjItMTItMDNUMTM6MDY6NDVaIiwidXNlcl9pZCI6IiJ9Xo8vu6VZZrGpc0YLX2vUwowPNlf_lA3KD6CsCbwsP5Aos6ykG9z1CbV537o-7LhQcTeIlmJT5-dS-3ylmeg0Cg',
                'Client-Session-Id': '2e28a036ca34b471',
                'Client-Version': '1c00aced-32cc-496a-b9b4-f4ecd307bbf9',
                'Connection': 'keep-alive',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Origin': 'https://www.twitch.tv',
                'Referer': 'https://www.twitch.tv/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            }
            data = '[{"operationName":"UsernameValidator_User","variables":{"username":"'+user+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'
            r = requests.post('https://gql.twitch.tv/gql', headers=headers, timeout=1, data=data).json()[0]['data']['isUsernameAvailable']
            if r == True:
                print(f"{Fore.MAGENTA}[{Fore.WHITE}+{Fore.MAGENTA}]{Fore.WHITE} Status: -{Fore.MAGENTA} [{Fore.BLUE}{user} : {Fore.BLUE} Available {Fore.MAGENTA}]")
                f.write(user + '\n')
            if r == False:
                print(f"{Fore.MAGENTA}[{Fore.WHITE}-{Fore.MAGENTA}]{Fore.WHITE} Status: -{Fore.MAGENTA} [{Fore.BLUE}{user} : {Fore.BLUE}Unavailable{Fore.MAGENTA}]")

def start():
    for _ in range(2):
        threading.Thread(target=check).start()

start()