import socket
#from gpiozero import LED
#from gpiozero import Buzzer
from time import sleep
from signal import pause
import adafruit_dht

def printa(frase):
    print(frase)
    #tcp.send(str(frase).encode())

def ligaLed(porta):
    led = LED(porta)
    led.on()

def desligaLed(porta):
    led = LED(porta)
    led.off()

def ligaAlarme(porta):
    led = LED(porta)
    led.on()
            
def desligaAlarme(porta):
    led = LED(porta)
    led.off

HOST = 'localhost'
PORT = 8082

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (HOST, PORT)

tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp.bind(origem)

tcp.listen(1)

print('Servidor central ligado.')

while True:

    conexao, cliente = tcp.accept()

    print('\nConexão realizada por:', cliente)

    while True:

        instrucao = conexao.recv(1024)
        estado = conexao.recv(1024)

        if not instrucao:

            break

        objeto = estado.decode()
        inicio = instrucao.decode()
                
        if inicio == 'ligar':
            if objeto == 'projetor':
                #ligaLed(25)
                printa('Projetor ligado.')
                
            if objeto == "lampada1":
                ligaLed(18)
                print("Lampada 1 ligada.")
                
            if objeto == 'lampada2':
                ligaLed(23)
                print("Lampada 2 ligada.")
                        
            if objeto == "arcondicionado":
                ligaLed(24)
                print("Arcondicionado ligado.")
            
            if objeto == "sensorDePresenca":
                print("sensorDePresenca")
            
            if objeto == "sensorDeFumaca":
                ligaLed(1)
                ligaAlarme(8)
            
            if objeto == "sensorDePorta":
                print("sensorDePorta")
            
            if objeto == "sensorDeJanela":
                print("sensorDeJanela")


        if inicio == "desligar":        
            if objeto == "projetor":
                desligaLed(25)
                print("Projetor desligado.")
                
            if objeto == "lampada1":
                desligaLed(18)
                            
            if objeto == 'lampada2':
                desligaLed(23)  
                        
            if objeto == "arcondicionado":
                desligaLed(24)
                
            if objeto == "sensorDePresenca":
                print("sensorDePresenca")
                
            if objeto == "sensorDeFumaca":
                desligaLed(1)
                desligaAlarme(8)
                
            if objeto == "sensorDePorta":
                print("sensorDePorta")    
            
            if objeto == "sensorDeJanela":
                print("sensorDeJanela")     
        
    print('Finalizando conexao do cliente', cliente)

    conexao.close()