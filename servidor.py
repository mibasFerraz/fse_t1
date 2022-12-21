import socket
from time import sleep

HOST = 'localhost'
PORT = 8082  

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (HOST, PORT)

tcp.connect(destino)

print('Cliente um ligado.\n')

while True:
       
    inicio = input("O que voce deseja fazer?(ligar/desligar/sair)\n")
    tcp.send(str(inicio).encode())
    if inicio == 'sair':
        break
    
    if inicio == 'ligar':
        objeto = input("O que voce deseja ligar?(projetor/ lampada1/ lampada2/ arcondicionado/ sensorDePresenca/ sensorDeFumaca/ sensorDePorta/ sensorDeJanela)\n")    
        tcp.send(str(objeto).encode())
        
    if inicio == 'desligar':
        objeto = input("O que voce deseja desligar?(projetor/ lampada1/ lampada2/ arcondicionado/ sensorDePresenca/ sensorDeFumaca/ sensorDePorta/ sensorDeJanela)\n")        
        tcp.send(str(objeto).encode())
    
    #sleep(10)
    #frase = tcp.recv(1024)
    #print(frase)
    
print('Volte sempre.')
tcp.close()