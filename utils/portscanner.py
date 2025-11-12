import socket
import sys
from urllib.parse import urlparse

class fkreyyPorts:
    def normalize_host(self, user_input):
        # aceita formatos: "https://exemplo.com", "exemplo.com:8080", "1.2.3.4"
        parsed = urlparse(user_input if "://" in user_input else "//" + user_input)
        host = parsed.hostname or user_input
        port_from_url = parsed.port
        return host, port_from_url

    def portscanners(self):
        ports = [21, 22, 80, 443, 445, 3306, 25]
        while True:
            try:
                falar = input("Digite IP/host (ou 'sair' para encerrar): ").strip()
                if not falar:
                    continue
                if falar.lower() in ("sair", "exit", "q"):
                    print("Encerrando.")
                    break

                host, port_from_url = self.normalize_host(falar)
                if port_from_url:
                    # se a URL já trouxe porta, testa só ela
                    ports_to_test = [port_from_url]
                else:
                    ports_to_test = ports

                print(f"Testando {host} nas portas: {ports_to_test}")
                for port in ports_to_test:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1.0)  # timeout mais tolerável
                    try:
                        code = sock.connect_ex((host, port))
                        if code == 0:
                            print(f"{port}: Porta ABERTA")
                        else:
                            print(f"{port}: Porta FECHADA/INACESSÍVEL (codigo {code})")
                    except socket.gaierror:
                        print("Erro: host inválido ou DNS não resolveu:", host)
                        break
                    except Exception as e:
                        print("Erro ao testar porta", port, "->", e)
                    finally:
                        sock.close()

            except KeyboardInterrupt:
                print("\nInterrompido pelo usuário. Saindo.")
                break
            except Exception as e:
                print("Erro inesperado:", e)

if __name__ == "__main__":
    scanner = fkreyyPorts()
    scanner.portscanners()