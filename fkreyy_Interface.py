import os
import fkreyy_codigo

def clear_screen():
    os.system("clear")

fkc = fkreyy_codigo.fkcode

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
        print("9 - Ransomware")
        print("10 - Botnet")
        print("0 - Sair")
        print("")
        
        while True:
            try:
                escolha = int(input("Selecione: "))
            except ValueError:
                os.kill()
                continue
            if escolha == 0:
                print("Saindo...")
                break

            elif escolha == 1:
                    clear_screen()
                    fkc.Scanners()

#---------------------------------------------------------



        

fkInterface.menu()


