from socket import *
import time

#Pegar o tempo inicial
tempo_inicial = time.time()

alvo = input ("Informe o ip para escanear: ")

ip_alvo = gethostbyname(alvo)

print ("Comecando scan: ", ip_alvo)
# Threading 
for i in range(50, 500):
    #IPv4
    #TCP
    s = socket(AF_INET, SOCK_STREAM)

    #Tento me conectar na porta
    conexao = s.connect_ex ((ip_alvo,i))

    if conexao == 0:
        print ("Porta: ", i , "Aberta)")
        s.close()


print ("Tempo que levou: ", time.time () - tempo_inicial)