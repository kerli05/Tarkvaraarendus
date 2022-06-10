import socket #impordib mooduli

s = socket.socket() #Loob socket objekti
host = socket.gethostname() # Otsib hostnamei
port = 8080 #pordi number
s.bind((host,port)) # saab serveri aadressi ja porti
s.listen(1) # kuulab kasutajat
print(host) # kontrollib, kas hostname on olemas
print("Waiting for any incoming connections ... ") #prindib teksti
conn, addr = s.accept()  # kuulab kasutajat
print(addr, "has connected to the server") #prindib teksti

filename = input(str("Please enter the filename of the file : ")) #prindib teksti
file = open(filename,'rb')  # avab faili
file_data = file.read(1024) # loeb faili
conn.send(file_data) # saadab faili
print("Data has been transmitted successfully") #prindib teksti