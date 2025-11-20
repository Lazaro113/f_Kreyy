from multiprocessing import Value
import os
import sys
import time
from utils.portscanner import fkreyyPorts
from tqdm import tqdm
from utils.brute_dns import ResolverDNS



def clear_screen():
    os.system("clear")

def loading():
    print("Iniciando processo...")

    
    for i in tqdm(range(10)):
        time.sleep(1.0)  

    print("Processo finalizado!")

class fkInterface:
    clear_screen()

    def menu():
        print("=========================================")  # menu principal
        print()
        print("██╗  ██╗   ██████╗    ███████╗██╗   ██╗")
        print("██║ ██╔╝   ██╔══██╗   ██╔════╝╚██╗ ██╔╝")
        print("█████╔╝    ██████╔╝   █████╗   ╚████╔╝ ")
        print("██╔═██╗    ██╔══██╗   ██╔══╝    ╚██╔╝  ")
        print("██║  ██╗██╗██║  ██║██╗███████╗██╗██║   ")
        print("╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝   ")
        print("")
        print("(=========================================)")
        print("")
        print("[ 01 ] - Scanners")
        print("[ 02 ] - Servidor")
        print("[ 03 ] - Phishing")
        print("[ 04 ] - IP")
        print("[ 05 ] - Discord")
        print("[ 06 ] - Ddos")
        print("[ 07 ] - Brute force")
        print("[ 08 ] - Keylogger")
        print("[ 09 ] - Malwares")
        print("[ 10 ] - Botnet")
        print("[ 12 ] - Sair do Programa")
        print("[ 0 ] - Sair")
        print("")

        while True:
            try:
                escolha_menu = int(input("Selecione: "))
                        
            except ValueError:
                print("Interrompido")
                sys.exit()
                
                
            if escolha_menu == 0:
                print("Saindo...")
                clear_screen()
                return fkInterface.menu()
                
            elif escolha_menu == 12:
                sys.exit()

            elif escolha_menu == 0o1:
                clear_screen()
                fkInterface.Scanners()

            elif escolha_menu == 0o2:
                clear_screen()
                fkInterface.Server()

            elif escolha_menu == 0o3:
                clear_screen()
                fkInterface.Phinshing()
                     
            elif escolha_menu == 0o4: 
                clear_screen()

            elif escolha_menu == 0o5:
                clear_screen()

            elif escolha_menu == 0o6:
                clear_screen()
                    
            elif escolha_menu == 0o7:
                clear_screen()
                fkInterface.Brute_Force()
                
            
            elif escolha_menu == 8:
                clear_screen()

            elif escolha_menu == 9:
                clear_screen()

    def Scanners():
        print("===========================")
        print("SCANNNERS DISPONIVEIS: ")
        print("===========================")
        print("")
        print("01 - NMAP")
        print("02 - METASPLOITS")
        print("03 - NETCAT")
        print("04 - HYDRA")
        print("05 - JOHN THE RIPPER")
        print("06 - AIRCRACK-NG")
        print("07 - WIRESHARK")
        print("08 - WIFI PINEAPPLE")
        print("0 - SAIR")

        while True:
            try:
                e_scanner = int(input("Selecione: "))
                
            except:
                print("Error...")

            match e_scanner:
                case 0:
                    print("Saindo....")
                    clear_screen()
                    fkInterface.menu()

                case 1:
                    clear_screen()
                    scanner = fkreyyPorts()  
                    scanner.portscanners()

                

                    
                    


    def Server():
        print("===========================")
        print("SERVIDORES DISPONIVEIS:")
        print("===========================")
        print("")
        print("01 - TCP")
        print("02 - UDP")
        print("03 - VPN")
        print("04 - LOCALHOST")
                

    def Phinshing():
        print("===========================")
        print("PHISHINGS DISPONIVEIS: ")
        print("===========================")
        print("01 - DISCORD")
        print("02 - GMAIL ")
        print("03 - YOUTUBE")
        print("04 - ")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    
    def Brute_Force():
        print("===========================")
        print("BRUTE FORCE'S DISPONIVEIS")
        print("===========================")
        print("01 - DNS RESOLVER")
        print("")
        print("")
        print("")
        print("")

        while True:
            try:
                e_bruteforce = int(input("Selecione: "))

            except:
                print("Erro.")

            match e_bruteforce:
                case 0:
                    print("Saindo...")
                    fkInterface.menu()
                    clear_screen()

                case 1:
                    clear_screen()
                    ResolverDNS.dnsbruto()

                

#---------------------------------------------------------



        

fkInterface.menu()


