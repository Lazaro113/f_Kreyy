import os
import fkreyy_codigo
import sys

def clear_screen():
    os.system("clear")

fkc = None

class fkInterface:
    clear_screen()

    def menu():
        print("=========================================")  # menu principal
        print("")
        print("██╗  ██╗   ██████╗    ███████╗██╗   ██╗")
        print("██║ ██╔╝   ██╔══██╗   ██╔════╝╚██╗ ██╔╝")
        print("█████╔╝    ██████╔╝   █████╗   ╚████╔╝ ")
        print("██╔═██╗    ██╔══██╗   ██╔══╝    ╚██╔╝  ")
        print("██║  ██╗██╗██║  ██║██╗███████╗██╗██║   ")
        print("╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝   ")
        print("")
        print("=========================================")
        print("1 - Scanners")
        print("2 - Servidor")
        print("3 - Phishing")
        print("4 - IP")
        print("5 - Discord")
        print("6 - Ddos")
        print("7 - Brute force")
        print("8 - Keylogger")
        print("9 - Malwares")
        print("10 - Botnet")
        print("0 - Sair")
        print("12 - Sair do Programa")
        print("")


        def Scanners():
                print("SCANNNERS DISPONIVEIS: ")
                print("")
                print("1 - NMAP")
                print("2 - METASPLOITS")
                print("3 - NETCAT")
                print("4 - HYDRA")
                print("5 - JOHN THE RIPPER")
                print("6 - AIRCRACK-NG")
                print("7 - WIRESHARK")
                print("8 - WIFI PINEAPPLE")
                print("0 - SAIR")


        def Server():
                print("SERVIDORES DISPONIVEIS:")
                print("")
                print("1 - TCP")
                print("2 - UDP")
                print("3 - VPN")
                print("4 - LOCALHOST")
                

        def Phinshing():
                print("PHISHINGS DISPONIVEIS: ")
                print("1 - DISCORD")
                print("2 - ")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                

        
        while True:
            try:
                escolha_menu = int(input("Selecione: "))
                
            except KeyboardInterrupt:
                print("Interrompido")
                sys.exit()
                clear_screen()
                continue
            
            if escolha_menu == 0:
                print("Saindo...")
                clear_screen()
                return fkInterface.menu()
            
            elif escolha_menu == 12:
                   sys.exit()

            elif escolha_menu == 0o1:
                    clear_screen()
                    Scanners()

            elif escolha_menu == 0o2:
                    clear_screen()
                    Server()


            elif escolha_menu == 0o3:
                    clear_screen()
                    Phinshing()
                 
            elif escolha_menu == 0o4: 
                    clear_screen()

            elif escolha_menu == 0o5:
                    clear_screen()

            elif escolha_menu == 0o6:
                    clear_screen()
                
            elif escolha_menu == 0o7:
                    clear_screen()
            
            
            

#---------------------------------------------------------



        

fkInterface.menu()


