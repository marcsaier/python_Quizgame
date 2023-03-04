#a simple quiz game designed by me :)
import json
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
    #abfrage ob es schon ein quiz mit dem namen gibt
    #
    #
    number_of_questions = input("Wie viele Fragen soll dein Quiz haben? :")
    for i in range(number_of_questions):
        insert_question()
    while True:    
        anotherone = input("Möchtest du noch eine Frage hinzufügen?(Y/N) :").lower()
        if anotherone == "y":
            while True:
                insert_question()
                anotherone = input("Möchtest du noch eine Frage hinzufügen?(Y/N) :").lower()
                if  anotherone == "n":
                    break
                elif anotherone != "y" or anotherone != "n":
                    anotherone = input("Ungültige Eingabe, versuche es erneut, Y = Ja, N = Nein :").lower()
            break
        elif anotherone == "n":
            break
        else:
            anotherone = input("Ungültige Eingabe, versuche es erneut, Y = Ja, N = Nein :").lower()
    with open(quiz_name+".json", "w+") as f:
        json.dump(questions, f)
    print("Dein Quiz wurde erstellt!")

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
