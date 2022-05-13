#Εισαγωγές των βιβλιοθηκών και κλάσεων που υλοποιήθηκαν για το πρόγραμμα
from tkinter import *
from LoginClass import Login
from mainProgramWindow import *
from tkinter import messagebox


#Δημιουργία παρθύρου σύνδεσης/εγγραφής για την εφαρμογή
loginWindow = Tk()
loginWindow.geometry("1280x720")
loginWindow.resizable(width=False, height=False)
loginWindow.config(background="#0600b5")
loginWindow.title("Face Recognition")

#Δήλωση μεταβλτών που περιέχουν τις εικόνες του background και του εικονιδίου
#του παρθύρου σύνδεσης/εγγραφής
icon = PhotoImage(file='gui_pictures/icon.png')
backroundImage = PhotoImage(file='gui_pictures/facerec.png')

#Τοποθέτηση εικονιδίου της μπάρας τίτλου
loginWindow.iconphoto(True, icon)

#Δημιουργία και τοποθέτηση εικόνας background
backround_label = Label(loginWindow,
              fg='#00FF00',
              bg='black',
              image=backroundImage)
backround_label.pack()

#Δημιουργία και τοποθέτηση επιγραφής "Face recognition/ Αναγνώριση Προσώπου"
#(Τίτλος προγράμματος)
label = Label(loginWindow,
              text="Face Recognition",
              font=('Arial',40,'bold'),
              fg='white',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)
label.place(x=0, y=0)

#Η μεταβλητή language χρησιμεύει παρακάτω για την αλλαγή της γλώσσας της εφαρμογής
language = False

#Συνάρτηση που ρυθμίζει την γλώσσα του προγράμματος
def swicharou():
    global language

    if language == False:
        loginWindow.title("Αναγνώριση Προσώπου")
        changeText(label, "Αναγνώριση Προσώπου")
        changeText(switch_to_sign_up_button, "Εγγραφή;")
        changeText(switch_to_login_button, "Σύνδεση;")
        changeText(languageButton, "Change Language")

        language = True

    else:
        loginWindow.title("Face Recognition")
        changeText(label, "Face Recognition")
        changeText(switch_to_sign_up_button, "Sign Up?")
        changeText(switch_to_login_button, "Login?")
        changeText(languageButton, "Αλλαγή Γλώσσας")


        language = False

#Συνάρτηση που αλλάζει το μύνημα ενός κουμπιού ή μιας επιγραφής
def changeText(thing, text):
        thing['text'] = text

#Δήλωση μεταβλτής που περιέχει την εικόνα του κουμπίου ρυθμίσεων
settingsPhoto = PhotoImage(file='gui_pictures/settings.png')

#Δημιουργία και τοποθέτηση κουμπίου ρυθμίσεων
languageButton = Button(loginWindow,
                command=swicharou,
                fg="black",
                bg="white",
                activeforeground="black",
                activebackground="white",
                font=("Comic Sans", 20),
                state=ACTIVE,
                text="Αλλαγή Γλώσσας",
                compound='bottom')
languageButton.place(x=1010, y=660)
#609
#Συνάρτηση που υλοποιεί ένα πεδίο εισόδου
def entrybox() :
    entry = Entry(loginWindow,
                  font=("Arial",20),
                  fg="black",
                  bg="white",
                  width=16)
    return entry

#Συνάρτηση που κωδικοποιεί το input του χρήστη σε UTF-8
#(απαραίτητο για το hashing των ταυτοποιητικών στοιχείων του χρήστη)
def infoEncode(checkbox):
    box = checkbox.get().encode("utf-8")

    return box

#Δήλωση μεταβλτών που περιέχουν τις εικόνες πίσω από
#τις μπάρες εισαγωγής στοιχείων του παρθύρου σύνδεσης/εγγραφής
login_photo = PhotoImage(file='gui_pictures/login.png')
sign_up_photo = PhotoImage(file='gui_pictures/sign_up.png')

#Δημιουργία επιγραφών που περιέχουν τις εικόνες πίσω από
#τις μπάρες εισαγωγής στοιχείων του παρθύρου σύνδεσης/εγγραφής
login_label = Label(loginWindow,
              fg='#00FF00',
              bg='grey',
              image=login_photo)

sign_up_label = Label(loginWindow,
              fg='#00FF00',
              bg='grey',
              image=sign_up_photo)

#Δήλωση μεταβλτών που περιέχουν τις εικόνες των κουμπιών "Login" και "Sign up"
login_button = PhotoImage(file='gui_pictures/login_button.png')
sign_up_button = PhotoImage(file='gui_pictures/sign_up_button.png')

#Δημιουργία των τριών απαραίτητων πεδίων εισαγωγής
#(username, password, retype password)
username_entrybox = entrybox()
password_entrybox = entrybox()
retype_password_entrybox = entrybox()

#Συνάρτηση που καλεί την μέθοδο login της κλάσης Login.
#Εαν η είσοδος του χρήστη στην εφαρμογή είναι επιτύχης, τότε μεταβιβαζόμαστε
#από το παράθυρο σύνδεσης/εγγραφής στο κεντρικό πάράθυρο της εφαρμογής
def loginClick():
    success = Login.login(infoEncode(username_entrybox), infoEncode(password_entrybox))

    if success == True:
        loginWindow.destroy()
        openMainWindow(language)

#Δημιουργία κουμπιού που ξεκινάει την διαδικασία εισόδου στην εφαρμογή
loginButton = Button(login_label,
                     text="Login",
                     command=loginClick,
                     font=("Comic Sans", 30),
                     fg="white",
                     bg="white",
                     activeforeground="white",
                     activebackground="white",
                     state=ACTIVE,
                     image=login_button)

#Συνάρτηση που καλεί την μέθοδο register της κλάσης Login
def signUpClick():
    success = Login.register(infoEncode(username_entrybox), infoEncode(password_entrybox), infoEncode(retype_password_entrybox))

    if success == False:
        messagebox.showwarning(title="Error", message="passwords do not match or password or name is to short")

#Δημιουργία κουμπιού που ξεκινάει την διαδικασία εγγραφής στην εφαρμογή
signUpButton = Button(sign_up_label,
                     text="Login",
                     command=signUpClick,
                     font=("Comic Sans", 30),
                     fg="white",
                     bg="white",
                     activeforeground="white",
                     activebackground="white",
                     state=ACTIVE,
                     image=sign_up_button)

#Η συνάρτηση placeHere είναι υπεύθυνη για την τοποθέτηση των πεδίων εισόδου,
#των εικόνων που βρίσκονται πίσω απο αυτά καθώς και το κουμπί "Login/Sign up"
def placeHere(label, button, xErntry, yErntry, switched, zEntry = None):
    label.place(x=30, y=200)

    xErntry.place(x=154, y=385)

    yErntry.place(x=154, y=433)
    yErntry.config(show="*")

    #Ανάλογα με το εάν ο χρήστης επιθύμει εγγραφή ή σύνδεση γίνονται οι κατάλληλες
    #αλλαγές στο γραφικό πεεριβάλλον
    if switched == False:

        button.place(x=160, y=295)
    else:
        zEntry.place(x=153, y=481)
        zEntry.config(show="*")

        button.place(x=160, y=330)

#Η συνάρτηση unplace αφαιρεί την ζητούμενη εικόνα που βρίσκεται πίσω από τα
#πέδία είσοδου, το κουμπί "Login/Sign up" και το πέδιο είσοδου retype password
#εαν χρειάζεται
def unplace (label, button, switched, zEntry = None):
    label.place_forget()

    button.place_forget()

    if switched == True:
        zEntry.place_forget()

#Η συνάρτηση switchButton_signUp και switchButton_login καλούν τις placeHere
#και unplace προκειμένου να να γίνει η αλλαγή από την λειτουργία σύνδεσης
#στην λειτουργία εγγραφής και το αντίθετο
def switchButton_signUp():
    switch_to_sign_up_button.place_forget()

    unplace(login_label,loginButton, False)

    placeHere(sign_up_label, signUpButton, username_entrybox, password_entrybox, True, retype_password_entrybox)

    switch_to_login_button.place(x=215, y=670)

def switchButton_login():
    switch_to_login_button.place_forget()

    unplace(sign_up_label,signUpButton, True, retype_password_entrybox)

    placeHere(login_label, loginButton, username_entrybox, password_entrybox, False)

    switch_to_sign_up_button.place(x=200, y=670)

#Δημιουργία των κουμπιών που εκτελούν τις συναρτήσεις switchButton_signUp
#και switchButton_login
switch_to_sign_up_button = Button(loginWindow,
                    text="Sign Up?",
                    font=("Comic Sans", 15),
                    state=ACTIVE,
                    command=switchButton_signUp)

switch_to_login_button = Button(loginWindow,
                    text="Login?",
                    font=("Comic Sans", 15),
                    state=ACTIVE,
                    command=switchButton_login)

#Αρχικοποιήση παραθύρου
placeHere(login_label,loginButton, username_entrybox, password_entrybox, False)
switch_to_sign_up_button.place(x=200, y=670)

loginWindow.mainloop()