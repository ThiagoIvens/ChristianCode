from threading import Thread
import time, socket
import datetime
import datetime
from datetime import timedelta

HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT_SERVIDOR = 1000    # Porta que o Servidor esta
PORT_USER = 2000        # Porta que o Cliente esta

def main(): 
    enviaProServidor()

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT_USER)
    tcp.bind(orig)
    tcp.listen(1)

    con, servidor = tcp.accept()
    print('Concetado por', servidor)
    try:
        while True:
            msg = con.recv(1024)
            if not msg: break
            print (servidor, msg)
            msg = msg.decode().split("|")
            t0 = msg[0].split(":")
            t0h = int(t0[0])
            t0min = int(t0[1])
            t0seg = int(t0[2])
            t0 = datetime.timedelta(hours=t0h, minutes=t0min, seconds=t0seg)
            # print(t0)

            t1 = msg[1].split(':')
            t1h = int(t1[0])
            t1min = int(t1[1])
            t1seg = int(t1[2])
            t1 = datetime.timedelta(hours=t1h, minutes=t1min, seconds=t1seg)
            # print(t1)

            t2 = msg[2].split(':')
            t2h = int(t2[0])
            t2min = int(t2[1])
            t2seg = int(t2[2])
            t2 = datetime.timedelta(hours=t2h, minutes=t2min, seconds=t2seg)
            # print(t2)

            t3 = datetime.datetime.now()
            # print("t3 -",t3.strftime("%H:%M:%S"))
            t3 = t3.strftime("%H:%M:%S").split(':')
            t3h = int(t3[0])
            t3min = int(t3[1])
            t3seg = int(t3[2])
            t3 = datetime.timedelta(hours=t3h, minutes=t3min, seconds=t3seg)

            t1_t0 = t1 - t0
            # print(t1_t0)
           
            t2_t3 = t2 - t3
            # print(t2_t3)
            total = t1_t0 + t2_t3            
            atraso = total/2
            
            # print(atraso, type(atraso))
            atual = datetime.datetime.now()
            # print(atual.strftime("%H:%M:%S"))
            '''
            atual = atual.strftime("%H:%M:%S").split(':')
            atual = datetime.timedelta( 
                hours=int(atual[0]), 
                minutes=int(atual[1]), 
                seconds=int(atual[2]) 
            )
            '''
            
            atualizada = atual + atraso
            print("Atualizada: ",atualizada.strftime("%H:%M:%S"))
    finally:
        print('Finalizando conexao com o servidor', servidor)
        con.close()

def enviaProServidor():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT_SERVIDOR)
    tcp.connect(dest)
    sair = input
    horaAtual = pegarHora()
    # trata a hora
    horaAtual = horaAtual.split()
    horaAtual = horaAtual[3].split(':')
    hora = int(horaAtual[0])
    min = int(horaAtual[1])
    seg = int(horaAtual[2])
    min -= 1

    # escreve a mensagem com hora, minutos e segundos
    msg = str(hora)+':'+str(min)+":"+str(seg)
    tcp.send (msg.encode('utf-8')) # envia
    tcp.close()

def pegarHora():
    return time.ctime()

if __name__ == "__main__":
    main()