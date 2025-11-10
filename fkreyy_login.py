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
                escolha = input("Digite sua senha: ")
                if escolha == "91939":
                    print("AcessoPermitido")
                    break

            except KeyboardInterrupt:
                print("AcessoNegado")
                sys.exit()
                
loginfkrey.loginkf()
    

                                                  
                                                  
                                                  