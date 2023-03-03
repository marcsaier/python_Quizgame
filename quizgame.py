#a simple quiz game designed by me :)

#Globale Variablen
questions = {}

#Eine Methode die, die Fragen und Antwortmöglichkeiten für unser Quiz definiert
def insert_question():
    question = input("Wie lautet die Frage? :")
    correct_answer = input("Wie ist die korrekte Antwort für die Frage? :")
    answers = ["A: "+input("Füllen sie die 4 Antwortmöglichkeiten aus:\nA =:"),
               "B: "+input("B =:"),
               "C: "+input("C =:"),
               "D: "+input("D =:")]
    questions[question] = {"correct_answer": correct_answer, "answers": answers}

#Diese Methode soll den Nutzer ein Quiz erstellen lassen
def create_quiz():
    print("Willkommen bei der Quizerstellung!")
    quiz_name = input("Wie soll dein Quiz heißen? :")
    number_of_questions = input("Wie viele Fragen soll dein Quiz haben? :")
    for i in range(number_of_questions):
        insert_question()
    anotherone = input("Bist du fertig mit deinem Quiz oder möchtest du noch eine Frage hinzufügen?(Y/N) :").lower()
    if anotherone == "y":
        insert_question()
    elif anotherone == "n":
        pass
        #scheibt quiz in datei und leitet zurück zum hauptmenü
    else:
        print("Ungültige Eingabe, versuche es erneut, Y = Ja, N = Nein :")


#Diese Methode soll abgerufen werden sobald das Quiz startet und Soll dem Nutzer das Quiz stellen
def new_game():
    print("WILLKOMMEN ZUM GROßEN QUIZ!")
    print("-------------------------------------")
    first_question = questions[list(questions.keys())[0]]
    print("Frage: " + list(questions.keys())[0])
    print("Antwortmöglichkeiten: " + str(first_question["answers"]))


def check_answer():
    pass

def display_score():
    pass

def play_again():
    pass
