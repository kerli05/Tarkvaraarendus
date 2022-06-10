from tkinter import * # Importib tkniteri

def register_user(): # Teeb funktsiooni register_user
    username_info = username.get() # Kasutajanimi väärtus on sisestatud kasutaja nimi
    password_info = password.get() # Parooli väärtus on sisestatud parooli väärtus

    file=open(username_info + ".txt", "w") # Teeb uue .txt kasutajanime nimega
    file.write(username_info+"\n") # Lisab esimesele reale kasutajanime
    file.write(password_info) # Lisab teisele reale parooli väärtuse
    file.close() # Paneb faili kinni

    username_entry.delete(0, END) # Kustutab registreerimis väljast sisestatud nime
    password_entry.delete(0, END) # Kustutab registreerimis väljast sisestatud parooli

    Label(screen1, text = "Registration Sucess", fg= "green", font = ("Calibiri", 11)).pack() # Kui registreerimine õnnestus kirjutab rohelise teksti et õnnestus

def register(): # Teeb funktsiooni register
    global screen1 # Teeb globaalse muutuja screen1
    screen1 = Toplevel(screen) # screen1 väärtus on Toplevel(screen) mis tuleb tkinter'ist
    screen1.title("Register") # Seab akna nimeks register
    screen1.geometry("300x250") # Seab akna suuruse 300x250

    global username # Teeb globaalse muutuja username
    global password # Teeb globaalse muutuja password
    global username_entry # Teeb globaalse muutuja username_entry
    global password_entry # Teeb globaalse muutuja password_entry
    username = StringVar() # StringVar on klass, mis pakub abifunktsioone selliste muutujate otseseks loomiseks ja juurdepääsemiseks selles tõlgis
    password = StringVar() # StringVar on klass, mis pakub abifunktsioone selliste muutujate otseseks loomiseks ja juurdepääsemiseks selles tõlgis

    Label(screen1, text = "Please enter details below").pack() # Teeb uue teksti et lisa oma detailid
    Label(screen1, text = "").pack() # # Teeb lahtri tühjaks
    Label(screen1, text = "Username * ").pack() # Teeb uue teksti lahtri jaoks Username
    username_entry = Entry(screen1, textvariable = username) # Võtab kasutajanime
    username_entry.pack() # Pack asutatakse selleks, et vidin täidaks kogu kaadri
    Label(screen1, text = "Password * ").pack() # Teeb uue teksti lahtri jaoks password
    password_entry = Entry(screen1, textvariable = password) # Võtab parooli
    password_entry.pack() # Pack asutatakse selleks, et vidin täidaks kogu kaadri
    Label(screen1, text = "").pack() # Teeb lahtri tühjaks
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack() #

def login(): # Teeb funktsiooni login
    print("Login session started") # Prindib et logimine algas kui vajutad login nuppu

def main_screen(): # Teeb uue funktsiooni main_screen
    global screen # Teeb globaalse muutuja screen
    screen = Tk() # Tk eksemplari loomine initsialiseerib selle interpretaatori ja loob juurakna
    screen.geometry("300x250") # Seab suuruseks 300x250
    screen.title("Notes 1.0") # Paneb akna nimeks Notes 1.0
    Label(text = "Notes 1.0", bg = "gray", width = "300", height = "2", font = ("Calibri", 13)).pack()# Teeb teksti Notes.10, halli värviga ja seab suuruse ja fondi
    Label(text = "").pack() # Teeb lahtri tühjaks
    Button(text="Login", height="2", width="30", command=login).pack() # Teeb logimis nupu
    Label(text= "").pack() # Teeb tühja lahtri
    Button(text = "Register", height = "2", width = "30", command = register).pack() # Teeb nupu register

    screen.mainloop() # Käsib aknal oodata, kuni kasutaja midagi teeb

main_screen() # Käivitab funktsiooni main_screen