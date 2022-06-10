import socket # Importib socketi
import sys # Importib sys
import time # Importib time

s = socket.socket() # Viis võrgu kahe sõlme ühendamiseks üksteisega suhtlemiseks
host = socket.gethostname() # Võtab aruti hostname
print("Server käivitub hostis: ", host) # Prindib arvuti host nime
port = 8082 # Seab pordiks 8082
s.bind((host, port)) # Seob pordi ja hosti
print("")
print("Server on hosti ja pordiga edukalt sidunud") # Prindib teksti
print("")
print("Server ootab sissetulevaid ühendusi") # Prindib teksti
print("")
s.listen(1) # Ootab ühendusi
conn, addr = s.accept() # Võtab ühenduse vastu
print(addr, "On serveriga ühenduses ja on nüüd võrgus...") # Prindib teksti
print("")
while 1: # Kasutatakse lõpmatu tsükli jaoks
    message = input(str(">>")) # Küsib sõnumit mida saata tahad
    message = message.encode() # Koodeerib teksti
    conn.send(message) # Saadab kliendile sõnumit
    print("Sõnum saadeti...") # Prindib sõnumi saatmise teate
    print("")
    incoming_message = conn.recv(1024)# Võtab kliendilt sõnumit
    incoming_message = incoming_message.decode()# Dekodeerib sõnum
    print(" Client: ", incoming_message) # Prindib sõnumi
    print("")