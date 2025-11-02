import os

def clear_screen():
    if os.name == "nt":      # Windows
        os.system("cls")
    else:                    # Linux / macOS / outros
        os.system("clear")

# uso
clear_screen()

print("=========================================")
print("")
print("██╗  ██╗   ██████╗    ███████╗██╗   ██╗")
print("██║ ██╔╝   ██╔══██╗   ██╔════╝╚██╗ ██╔╝")
print("█████╔╝    ██████╔╝   █████╗   ╚████╔╝ ")
print("██╔═██╗    ██╔══██╗   ██╔══╝    ╚██╔╝  ")
print("██║  ██╗██╗██║  ██║██╗███████╗██╗██║   ")
print("╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝   ")
print("")
print("=========================================")
print("")
print(input("Selecione:"))
print("")
print("")
