import socket #impordib socketi
import sys # impordib sys
import time # impordib time

s = socket.socket()  # Loob socket objekti
host = input(str("Sisestage serveri hostinimi:")) #Hosti nimi
port = 8082 # määrab pordi
s.connect((host, port)) #ühendab hosti
print("Ühendatud vestlusserveriga") #Prindib ühenduse teade
while 1: # Kasutatakse lõpmatu tsükli jaoks
    incoming_message = s.recv(1024) #Võtab kliendilt sõnumit
    incoming_message = incoming_message.decode() # Dekodeerib sõnum
    print(" Server: ", incoming_message) #Prindib sõnumi
    print("") #Prindib tühja rea
    message = input(str(">>")) # Küsib klientilt sõnumit
    message = message.encode() # Kodeerib sõnum
    s.send(message) # Saadab kliendilt sõnumi
    print("Sõnum saadeti...") #prindib sõnumi saatmise teate
    print("") #Prindib tühja rea