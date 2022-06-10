import socket #impordib mooduli
s = socket.socket()# Loob socket objekti
host = input(str("Please enter the hpst address of the sender : ")) #prindib teksti
port = 8080 # pordi number
s.connect((host,port)) #saab serveri aadressi ja porti
print("Connected ... ") #prindib teksti

filename = input(str("Please enter a filename for the incoming file : ")) #prindib teksti
file = open(filename, 'wb') # avab faili
file_data = s.recv(1024)  # saadab faili
file.write(file_data) # kirjutab faili
file.close() # sulgeb faili
print("File has been received successfully.") #prindib teksti