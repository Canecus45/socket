primo=float(input("Inserisci un numero:\n>"))
operazione=input("Inserisci un operazione:\n>")
secondo=float(input("Inserisci un numero:\n>"))

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

print(risultato)