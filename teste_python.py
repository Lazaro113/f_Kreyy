import socket 

ip = "127.0.0.1"
host = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,host))
s.listen(1)
print(f"Aguardando conexão {host}")

con, cliente = s.accept()
print("Conectado com sucessso!!!")

while True: 
	msg = input("> ")
	if msg == "sair":
		s.close()
		break
	msg += "\n"
	con.send(msg.encode())

	dados = con.recv(1024)
	print(dados.decode())

else:
	s.close
