# pegar a hora a atual, e fazer um socket para receber a mensagem com a hora do cliente
from threading import Thread
import time, socket

HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT_SERVIDOR = 1000    # Porta que o Servidor esta
PORT_USER = 2000        # Porta que o Cliente esta

t1 = 0
t2 = 0
t3 = 0

def main(): 
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT_SERVIDOR)
    tcp.bind(orig)
    tcp.listen(1)

    con, cliente = tcp.accept()
    print('Concetado por', cliente)
    msg = con.recv(1024)
    t0 = msg.decode()
    
    print("t0 ", t0)

    t1 = pegarHora()
    t1 = t1.split()
    t1 = t1[3]

    time.sleep(5)
    
    enviaProCliente(t0, t1)

    print('Finalizando conexao do cliente', cliente)
    con.close()

def enviaProCliente(t0, t1): # https://wiki.python.org.br/SocketBasico
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT_USER)
    tcp.connect(dest)
    t2 = pegarHora()
    t2 = t2.split()
    t2 = t2[3]
    print("t2 ", t2)

    # escreve a mensagem com hora, minutos e segundos
    msg = str(t0) +"|"+ str(t1) + "|" + str(t2)
    print(msg)
    tcp.send (msg.encode('utf-8')) # envia
    tcp.close()

def pegarHora():
    return time.ctime()

if __name__ == "__main__":
    main()