from requests  import post
from colorama  import Fore
from os        import system
from random    import choices
from threading import Thread

system('cls')
class twitch:
    def __init__(self):
        self.checked  = 0
        self.valid    = 0
        self.invalid  = 0
        self.errors   = 0
        self.threads  = 10

        self.title_c  = "{TUC}"
    def threadings(self):
        for _ in range(int(self.threads)):
            Thread(target=twitch().checker()).start()

    def checker(self):
        while True:
            self.username = ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=4))
            system(f"title {self.title_c} (Made By Sokisa#1994)^| checked: {self.checked}^| valid: {self.valid}^| invalid: {self.invalid}^| errors: {self.errors}")
            headers = {
                'Accept-Language': 'en-US',
                'Accept': '*/*',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
                'Connection': 'keep-alive',
                'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
            }
            data = '[{"operationName":"UsernameValidator_User","variables":{"username":"'+self.username+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'

            req = post('https://gql.twitch.tv/gql', headers=headers, data=data)

            if req.json()[0]['data']['isUsernameAvailable'] == True:
                print(f"{Fore.CYAN}[{Fore.BLUE}+{Fore.CYAN}]{Fore.BLUE} {self.username} {Fore.CYAN}Available {Fore.RESET}")
                self.valid += 1

            elif req.json()[0]['data']['isUsernameAvailable'] == False:
                print(f"{Fore.CYAN}[{Fore.RED}-{Fore.CYAN}]{Fore.RED} {self.username} {Fore.CYAN}Taken {Fore.RESET}")
                self.invalid += 1    
            else:
                print(f"{Fore.CYAN}[{Fore.LIGHTRED_EX}!{Fore.CYAN}] {Fore.LIGHTRED_EX}Error{Fore.RESET}")
                self.errors += 1

twitch().threadings()
