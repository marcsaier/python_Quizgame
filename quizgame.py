#a simple quiz game designed by me :)

#Globale Variablen
questions = {}

#Eine Methode die, die Fragen und Antwortmöglichkeiten für unser Quiz definiert
def insert_questions():
    question = input("Wie lautet die Frage? :")
    correct_answer = input("Wie ist die korrekte Antwort für die Frage? :")
    answers = ["A: "+input("Füllen sie die 4 Antwortmöglichkeiten aus:\nA =:"),
               "B: "+input("B =:"),
               "C: "+input("C =:"),
               "D: "+input("D =:")]
    questions[question] = {"correct_answer": correct_answer, "answers": answers}

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
