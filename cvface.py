#Εισαγωγές των βιβλιοθηκών και κλάσεων που υλοποιήθηκαν για το πρόγραμμα
import face_recognition
import cv2
import numpy as np
import os

#Η συνάρτηση findEncodings παίρνει τις εικόνες των γνωστών προσώπων
#και τις κωδικοποιεί
def findEncodings(images):
    encodeList = []
    for img in images:
        #Μετατροπή των εικόνων σε RGB από BGR για ευκολότερο encoding που χρησιμοποιεί η βιβλιοθήκη face_recognition
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def recognition():
    #Δέσμευση κάμερας
    video_capture = cv2.VideoCapture(0)

    path = 'img/known'
    known_face_images = []
    known_face_names = []
    dirlist = os.listdir(path)

    for i in dirlist:
        current = cv2.imread(f'{path}/{i}')
        known_face_images.append(current)

        known_face_names.append(os.path.splitext(i)[0])

    # Αρχικοποίηση μερικών μεταβλητών
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    known_face_encodings = findEncodings(known_face_images)

    while True:
        # Επιλογή ενός frame από το βίντεο
        ret, frame = video_capture.read()

        # Σμίκρυνση του frame στο 1/4 για γρηγορότερη επεξεργασία
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Μετατροπή εικόνας από BGR σε RGB που χρησιμοποιεί η βιβλιοθήκη face_recognition
        rgb_small_frame = small_frame[:, :, ::-1]

        # Επεξεργασία ενός frame και του επόμενου
        if process_this_frame:
            # Εύρεση όλων των προσώπων και κωδικοποίηση τους από κάθε frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # Έλεγχος γνωστού προσώπου στο βίντεο με άγνωστο
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.55)
                name = "Unknown"

                # Ταυτίζει το πρόσωπο που βρίσκεται στο βίντεο με το πρόσωπο που διαφέρει λιγότερο
                # από τα γνωστά πρόσωπα
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Εμφάνιση αποτελεσμάτων
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Δημιουργία ενός τετραγώνου γύρο από το πρόσωπο
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Δημιουργία ετικέτας με το όνομα του προσώπου κάτω από αυτό
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Εμφάνιση της εικόνας
        cv2.imshow('Video', frame)

        # Το 'q' κλείνει την αναγνώριση
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Αποδέσμευση κάμερας και παραθύρου
    video_capture.release()
    cv2.destroyAllWindows()


   #  _.---.._             _.---...__
   # .-'   /\   \          .'  /\     /
   # `.   (  )   \        /   (  )   /
   #   `.  \/   .'\      /`.   \/  .'
   #     ``---''   )    (   ``---''
   #             .';.--.;`.
   #           .' /_...._\ `.
   #         .'   `.a  a.'   `.
   #        (        \/        )
   #         `.___..-'`-..___.'
   #            \          /
   #             `-.____.-'