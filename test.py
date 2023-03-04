#Hier werden Dinge ausprobiert...
#Optimal bin ich leer...
import json
questions = {}

def insert_questions():
    question = input("Wie lautet die Frage? :")
    correct_answer = input("Wie ist die korrekte Antwort für die Frage? :")
    answers = ["A: "+input("Füllen sie die 4 Antwortmöglichkeiten aus:\nA =:"),
               "B: "+input("B =:"),
               "C: "+input("C =:"),
               "D: "+input("D =:")]
    questions[question] = {"correct_answer": correct_answer, "answers": answers}


#first_question = questions[list(questions.keys())[0]]
#print("Frage: " + list(questions.keys())[0])
#print("Antwortmöglichkeiten: " + str(first_question["answers"]))

def create_quiz():
    print("Willkommen bei der Quizerstellung!")
    quiz_name = input("Wie soll dein Quiz heißen? :")
    number_of_questions = int(input("Wie viele Fragen soll dein Quiz haben? :"))
    for i in range(number_of_questions):
        insert_questions()
    anotherone = input("Bist du fertig mit deinem Quiz oder möchtest du noch eine Frage hinzufügen?(Y/N) :").lower()
    if anotherone == "y":
        insert_questions()
    elif anotherone == "n":
        #überprüfen ob schon ein quiz mit dem namen existiert???
        with open(quiz_name+".json", "w+") as f:
            json.dump(questions, f)

create_quiz()