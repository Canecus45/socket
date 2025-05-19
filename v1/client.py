import json
import socket

SERVER_IP='127.0.0.1'
SERVER_PORT=50005
BUFFER_SIZE=1024
NUM_MESSAGES=1

# Creazione dei socket
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(NUM_MESSAGES):
    primoNumero=float(input("Inserisci un numero:\n>"))
    operazione=input("Inserisci un operazione:\n>")
    secondoNumero=float(input("Inserisci un numero:\n>"))

    messaggio={"primoNumero":primoNumero,
            "operazione":operazione,
            "secondoNumero":secondoNumero
            }

    messaggio=json.dumps(messaggio)

    sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP,SERVER_PORT))
    data,addr=sock.recvfrom(BUFFER_SIZE)
    print("Messaggio ricevuto dal server {addr}: {data.decode}")

# Chiusura del socket
sock.close