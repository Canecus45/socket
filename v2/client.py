import json
import socket

# Client
import socket

HOST = '127.0.0.1'  # Indirizzo del server
PORT = 65432        # Porta usata dal server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    primoNumero=float(input("Inserisci un numero:\n>"))
    operazione=input("Inserisci un operazione:\n>")
    secondoNumero=float(input("Inserisci un numero:\n>"))

    messaggio={"primoNumero":primoNumero,
            "operazione":operazione,
            "secondoNumero":secondoNumero
            }
    sock_service.sendall(messaggio) # invio direttamente in formato byte
    data = sock_service.recv(1024) # Il parametro indica la dimensione massima dei dati che possono essere ricevuti in una sola volta

# A questo punto la socket è stata chiusa automaticamente
print('Received', data.decode())
