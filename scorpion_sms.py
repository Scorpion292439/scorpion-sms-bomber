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

def darkfly_installer():
    system("clear")
    print(f"{Fore.RED + Style.BRIGHT}╔══════════════════════════════════════════════════════════╗")
    print(f"║                   DARKFLY TOOL KURULUM                   ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}DarkFly kuruluyor, lütfen bekleyin...{Style.RESET_ALL}\n")

    commands = [
        "pkg install python2 -y",
        "pkg install git -y",
        "git clone https://github.com/Ranginang67/DarkFly-Tool",
        "cd DarkFly-Tool && python2 install.py"
    ]

    for cmd in commands:
        print(f"{Fore.CYAN}[RUN] {cmd}{Style.RESET_ALL}")
        result = system(cmd)
        if result != 0 and "cd" not in cmd and "install.py" not in cmd:
            print(f"{Fore.RED}Hata oluştu! Manuel kurulum yap.{Style.RESET_ALL}")
            sleep(5)
            return
        sleep(1)

    # KURULUM TAMAM - BÜYÜK DARKFLY EKRANI
    system("clear")
    print("\n" * 4)
    print(f"{Fore.MAGENTA + Style.BRIGHT}                ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ██╗   ██╗")
    print(f"                ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗╚██╗ ██╔╝")
    print(f"                ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝ ╚████╔╝ ")
    print(f"                ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗  ╚██╔╝  ")
    print(f"                ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║   ██║   ")
    print(f"                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN + Style.BRIGHT}                   KURULUM TAMAMLANDI!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW + Style.BRIGHT}     Artık sadece \"DarkFly\" yazarak çalıştırabilirsin{Style.RESET_ALL}\n")
    sleep(3)

    # OTOMATİK OLARAK "DarkFly" YAZIP ENTER BASIYOR!
    print(f"{Fore.CYAN}DarkFly başlatılıyor...{Style.RESET_ALL}")
    sleep(2)
    system("DarkFly")  # İşte bu satır: "DarkFly" yazıp Enter basıyor!

    # DarkFly kapanınca Scorpion'a geri dön
    print(f"\n{Fore.YELLOW}DarkFly kapatıldı.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Ana menüye dönmek için Enter'a bas...{Style.RESET_ALL}")
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
                          f"{Fore.CYAN}║ 1. {Fore.GREEN}SMS Bomber                {Fore.WHITE}║{Style.RESET_ALL}\n"
                          f"{Fore.CYAN}║ 2. {Fore.MAGENTA}DarkFly Tool Kur & Başlat {Fore.WHITE}║{Style.RESET_ALL}\n"
                          f"{Fore.CYAN}║ 3. {Fore.RED}Çıkış                     {Fore.WHITE}║{Style.RESET_ALL}\n"
                          f"{Fore.MAGENTA + Style.BRIGHT}╚{'═' * 42}╝{Style.RESET_ALL}\n\n"
                          f"{Fore.YELLOW}Seçim → {Fore.GREEN}")
            secim = int(secim)
        except:
            print(f"{Fore.RED}Geçersiz giriş!{Style.RESET_ALL}")
            sleep(2)
            continue

        if secim == 1:
            print("SMS Bomber yakında eklenecek...")  # Buraya senin SMS bomber menünü ekleyeceksin
            sleep(2)
        elif secim == 2:
            darkfly_installer()
        elif secim == 3:
            print(f"{Fore.RED + Style.BRIGHT}Çıkış yapılıyor... Güle güle!{Style.RESET_ALL}")
            sleep(2)
            sys.exit(0)
        else:
            print(f"{Fore.RED}Geçersiz seçim!{Style.RESET_ALL}")
            sleep(2)

if __name__ == "__main__":
    main()