#Εισαγωγές των βιβλιοθηκών και κλάσεων που υλοποιήθηκαν για το πρόγραμμα
import face_recognition as fr
import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

#Η συνάρτηση findEncodings παίρνει τις εικόνες των γνωστών προσώπων
#και τις κωδικοποιεί
def findEncodings(images):
    list_people_encoding = []

    for filename in os.listdir(images):
        known_image = fr.load_image_file(f'{images}{filename}')
        known_encoding = fr.face_encodings(known_image)[0]

        list_people_encoding.append((known_encoding, filename))

    return list_people_encoding


def find_target_face():
    #Εύρεση προσώπων στην επιλεγμένη εικόνα
    face_location = fr.face_locations(target)

    for person in findEncodings('img\known/'):
        encoded_face=person[0]
        filename = person[1]

        #Σύγκριση επιλεγμένου προσώπου με τα ήδη γνωστά
        is_target = fr.compare_faces(encoded_face, target_encoding, tolerance=0.55)

        if face_location:
            face_number = 0
            for location in face_location:
                if is_target[face_number]:
                    label = filename
                    create_frame(location, label)

            face_number +=1

#Η συνάρτηση create_frame εμφανίζει τα αποτελεσμάτα
def create_frame(location, label):
    top, right, bottom, left = location

    # Δημιουργία ενός τετραγώνου γύρο από το πρόσωπο
    cv2.rectangle(target, (left, top), (right, bottom), (0, 0, 255), 2)

    # Δημιουργία ετικέτας με το όνομα του προσώπου κάτω από αυτό
    cv2.rectangle(target, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(target, label, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)

# Η συνάρτηση show_image εμφανίζει την εικόνα
def show_image():
    rgb_img = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)
    cv2.imshow(("Face Recognition"), rgb_img)
    cv2.waitKey(0)

# συνάρτηση photoRecognition μας επιτρέπει να επιλέξουμε την εικόνα που θέλουνε να
# αναγνωρίσουμε και να ξεκινήσουμε την αναγνώριση
def photoRecognition():
    load_image = askopenfilename()

    global target
    target = fr.load_image_file(load_image)
    global target_encoding
    target_encoding= fr.face_encodings(target)

    find_target_face()
    show_image()