import fkreyy_login
import fkreyy_Interface

fk = fkreyy_Interface.fkInterface
fkl = fkreyy_login.loginfkrey

try:
    while True:
        fkl.loginkf()
        fk.menu()
        
except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário (Ctrl+C). Finalizando com cuidado...")
        pass


