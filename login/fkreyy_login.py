import os
import sys

def clearscreen():
    os.system("clear")

class loginfkrey:
    clearscreen()
    def loginkf():
        print("  ___       ________  ________  ___  ________    ")   
        print(" |\  \     |\   __  \|\   ____\|\  \|\   ___  \  ")  
        print(" \ \  \    \ \  \|\  \ \  \___|\ \  \ \  \\ \  \ ")   
        print("  \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \\ \  \ ")  
        print("   \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \\ \  \ ") 
        print("    \ \_______\ \_______\ \_______\ \__\ \__\\ \__\ ")
        print("     \|_______|\|_______|\|_______|\|__|\|__| \|__|  ")        
        print("")
        while True:
            try:
                usuario = input("Digite seu Usuário: ")
                senha = input("Digite sua senha: ")
                if senha == "91939":
                    print("AcessoPermitido")
                    break
                elif usuario == "Kreyy0Sec":
                    print("Usuario Cadastrado")

            except KeyboardInterrupt:
                print("AcessoNegado")
                sys.exit()
                
loginfkrey.loginkf()
    

                                                  
                                                  
                                                  