import json
import socket

SERVER_IP='127.0.0.1'
SERVER_PORT=50005
BUFFER_SIZE=1024

# Creazione del socket
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT))

print("Server in attesa di messaggi...")

while True:
    # Ricezione dei dati dal client
    data,addr=sock.recvfrom(BUFFER_SIZE)
    print("Mesaggio ricevuto dal client {addr}: {datadecode()}")
    if not data:
        break

    data = data.decode()
    data = json.loads(data)
    
    primo=data["primoNumero"]
    operazione=data["operazione"]
    secondo=data["secondoNumero"]

    if primo>secondo:
        if operazione == "+":
            risultato=primo+secondo
        elif operazione == "-":
           risultato=primo-secondo
        elif operazione == "*":
            risultato=primo*secondo
        elif operazione == "/":
            risultato=primo/secondo
    else:
        if operazione == "+":
            risultato=secondo+primo
        elif operazione == "-":
            risultato=secondo-primo
        elif operazione == "*":
            risultato=primo*secondo
        elif operazione == "/":
            risultato=secondo/primo
    # Invio di una risposta al client
    reply = f"{risultato}"
    sock.sendto(reply.encode(), addr)