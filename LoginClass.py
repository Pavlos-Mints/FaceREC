from hashforpass import hashing

class Login:

    #Η συνάρτηση login είναι υπεύθυνη για τον έλεγχο των στοιχείων του χρήστη
    @staticmethod
    def login(name, password):
        success = False
        with open("user_detail", "r") as file:
            for i in file:
                #Χωρίζονται τα στοιχεία του χρήστη που είναι ήδη αποθηκευμένα στον
                #φάκελο user_detail
                a, b = i.split(",")
                b = b.strip()
                #Εδώ γίνονται hash και σύγκριση των στοιχείων που έδωσε ο χρήστης με
                #με αυτά που είναι αποθηκευμένα στον φάκελο user_detail
                if a == hashing(name).hexdigest() and b == hashing(password).hexdigest():
                    success = True
                    break

        if success:
            return True

    # Η συνάρτηση register είναι υπεύθυνη για την εγγραφή του χρήστη.
    @staticmethod
    def register(name, password, retype_password):
        #Εάν το password είναι ίδιο με το retype_password τότε τα στοιχεία του χρήατη
        #γίνονται hash και γράφονται στον φάκελο user_detail
        if (password == retype_password and len(password) >= 8 and len(name) > 0):
            with open("user_detail", "a") as file:
                file.write("\n" + str(hashing(name).hexdigest()) + "," + str(hashing(password).hexdigest()))
        else:
            return False

