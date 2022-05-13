#Εισαγωγές των βιβλιοθηκών και κλάσεων που υλοποιήθηκαν για το πρόγραμμα
from tkinter import *
from cvface import *
from photoRecognition import *
import os

#Δήλωση μεταβλτών που περιέχουν τις εικόνες του background και του εικονιδίου
#του κύριου παραθύρου
global icon1
global backroundImage1

#Η συνάρτηση openMainWindow δημιουργεί το κύριο παρθύρο για την εφαρμογή
def openMainWindow(language):
    global mainWindow
    mainWindow = Tk()
    mainWindow.geometry("1280x720")
    mainWindow.resizable(width=False, height=False)
    mainWindow.config(background="#0600b5")

    # Ανάθεση μεταβλτών που περιέχουν τις εικόνες του background και του εικονιδίου
    # του κύριου παραθύρου
    icon1 = PhotoImage(file='gui_pictures/icon.png')
    backroundImage1 = PhotoImage(file='gui_pictures/facerec.png')

    # Τοποθέτηση εικονιδίου της μπάρας τίτλου
    mainWindow.iconphoto(True, icon1)

    backround_label = Label(mainWindow,
                            fg='#00FF00',
                            bg='black',
                            image=backroundImage1)
    backround_label.pack()

    # Δημιουργία και τοποθέτηση επιγραφής "Face recognition/ Αναγνώριση Προσώπου"
    # (Τίτλος προγράμματος)
    label1 = Label(mainWindow,
                  text="Face Recognition",
                  font=('Arial', 40, 'bold'),
                  fg='white',
                  bg='black',
                  relief=RAISED,
                  bd=10,
                  padx=20,
                  pady=20)
    label1.place(x=0, y=0)

    if language == False:
        #Τοποθέτηση κούμπιών κύριου παραθύρου που ξεκινούν τις λειτουργίες τις εφαρμογής
        #στα αγγλικά
        button(mainWindow, openUnknown, 180, 230, "Add Unknown Faces")

        button(mainWindow, openKnown, 180, 310, "Add Known Faces")

        button(mainWindow, recognition, 180, 390, "Begin Live Recognition")

        button(mainWindow, photoRecognition, 180, 470, "Begin Photo Recognition")

        button(mainWindow, exit, 180, 550, "Exit App")

        mainWindow.title("Face Recognition")

        label1.config(text="Face Recognition")

    elif language == True:
        # Τοποθέτηση κούμπιών κύριου παραθύρου που ξεκινούν τις λειτουργίες τις εφαρμογής
        # στα ελληνικά
        button(mainWindow, openUnknown, 180, 230, "Προσθήκη Άγνωστου Προσώπου")

        button(mainWindow, openKnown, 180, 310, "Προσθήκη Γνωστού Προσώπου")

        button(mainWindow, recognition, 180, 390, "Έναρξη αναγνώρισης από βίντεο")

        button(mainWindow, photoRecognition, 180, 470, "Έναρξη αναγνώρισης φωτογραφίας")

        button(mainWindow, exit, 180, 550, "Έξοδος")

        mainWindow.title("Αναγνώριση προσώπου")

        label1.config(text="Αναγνώριση προσώπου")

    mainWindow.mainloop()

#Η συνάρτηση button βοηθάει στην ευκολότερη τοποθέτηση των κουμπιών στο κύριο παράθυρο
def button(window, function, xf, yf, txt):
    button = Button(window,
                    command=function,
                    activeforeground="black",
                    activebackground="white",
                    font=("Comic Sans", 15),
                    state=ACTIVE,
                    image=None,
                    text=txt,
                    compound='bottom')
    button.place(x=xf, y=yf)

#Οι συναρτήσεις openKnown και openUnknown ανοίγουν τους φακέλους που αποθυκεύουν
#τα γνωστά και τα άγνωστα πρόσωπα αντίστοιχα
def openKnown():
    os.startfile(r'img\known')

def openUnknown():
    os.startfile(r'img\unknown')

# Η συνάρτηση exit κλείνει την εφαρμογή
def exit():
    mainWindow.destroy()
