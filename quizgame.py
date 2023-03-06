#a simple quiz game designed by me :)
import json
import os

#Globale Variablen
questions = {}

#Eine Methode die, die Fragen und Antwortmöglichkeiten für unser Quiz definiert
def insert_question():
    question = input("Wie lautet die Frage? :")
    correct_answer = input("Welche Antwortmöglichkeit ist richtig A, B, C oder D:").lower()
    while True:
        if correct_answer !="a" and correct_answer !="b" and correct_answer !="c" and correct_answer !="d":
            print("Die korrekte Antwort muss einer der Möglichkeiten A, B, C oder D entsprechen")
            correct_answer = input("Wie ist die korrekte Antwort für die Frage? :").lower()
        else:
            break
    answers = ["A: "+input("Füllen sie die 4 Antwortmöglichkeiten aus:\nA =:"),
               "B: "+input("B =:"),
               "C: "+input("C =:"),
               "D: "+input("D =:")]
    questions[question] = {"correct_answer": correct_answer, "answers": answers}

#Diese Methode soll den Nutzer ein Quiz erstellen lassen
def create_quiz():
    print("Willkommen bei der Quizerstellung!")
    quiz_name = str(input("Wie soll dein Quiz heißen? :"))
    while os.path.exists("saved_quiz/"+quiz_name+".json"):
        quiz_name = input("Es existiert bereits ein Quiz mit diesem Namen!\nBitte Lege einen neuen Namen fest: ")
    number_of_questions = int(input("Wie viele Fragen soll dein Quiz haben? :"))    #Was passiert wenn keine Zahl angeben wird???
    for i in range(number_of_questions):
        insert_question()
    anotherone = input("Möchtest du noch eine Frage hinzufügen?(Y/N) :").lower()
    while True:    
        if anotherone == "y":
            while True:
                insert_question()
                anotherone = input("Möchtest du noch eine Frage hinzufügen?(Y/N) :").lower()
                if  anotherone == "n":
                    break
                elif anotherone != "y" or anotherone != "n":
                    anotherone = input("Ungültige Eingabe, versuche es erneut, Y = Ja, N = Nein :").lower()
        elif anotherone == "n":
            break
        else:
            anotherone = input("Ungültige Eingabe, versuche es erneut, Y = Ja, N = Nein :").lower()
    if not os.path.exists("saved_quiz"):
        os.makedirs("saved_quiz")
    with open("saved_quiz/"+quiz_name+".json", "w+") as f:
        json.dump(questions, f)
    print("Dein Quiz wurde erstellt!\nDu kommst zurück zum Hauptmenü...")

#Diese Methode soll das entsprechende Quiz aus der .json Datei in das Dictionary laden
def load_quiz():
    questions = {}
    quiz_path = "saved_quiz"
    quizzes = os.listdir(quiz_path)
    quizzes_names = [os.path.splitext(file)[0] for file in quizzes]
    if quizzes_names == []:
        print("Es gibt leider kein gespeichertes Quiz für dich :(\nBitte erstelle ein Quiz")
        main_menu()
    for i in range(len(quizzes_names)):
        print("["+str(i)+"]"+": "+quizzes_names[i])
    user_choice = int(input("Bitte wähle das Quiz aus, dass du spielen möchtest : "))
    try:
        with open(os.path.join(quiz_path, quizzes_names[user_choice]+".json")) as f:
            questions = json.load(f)
    except IndexError:
        print("Ungültige Eingabe (Index Error)")
        load_quiz()
    except FileNotFoundError:
        print("Leider konnte das Quiz nicht geladen werden :( (File not found)")
    except json.JSONDecodeError:
        print("Leider konnte das Quiz nicht geladen werden :( (json.JSONDecodeError)")
    return questions

#Diese Methode soll den Nutzer Quizzes löschen lassen
def delete_quiz():
    quiz_path = "saved_quiz"
    quizzes = os.listdir(quiz_path)
    quizzes_names = [os.path.splitext(file)[0] for file in quizzes]
    if quizzes_names == []:
        print("Es gibt derzeit keine gespeicherten Quizzes :(\nDu kannst Quizzes im Hauptmenü erstellen")
        main_menu()
    for i in range(len(quizzes_names)):
        print("["+str(i)+"]"+": "+quizzes_names[i])
    user_choice = int(input("Bitte wähle das Quiz aus, dass du löschen möchtest : "))
    try:
        os.remove(os.path.join(quiz_path, quizzes_names[user_choice] + ".json"))
        print("Quiz erfolgreich gelöscht!")
    except IndexError:
        print("Ungültige Eingabe (Index Error)")
        delete_quiz()
    except FileNotFoundError:
        print("Leider konnte das Quiz nicht gefunden werden :( (File not found)")

#Diese Methode soll dem Nutzer das Quiz stellen
def play_quiz():
    print("WÄHLE DAS QUIZ DAS DU SPIELEN MÖCHTEST")
    print("-------------------------------------")
    questions = load_quiz()
    print("Los Geht's")
    score = 0
    num_questions = len(questions)
    for i, question in enumerate(questions.values()):
        print(f"\nFrage {i+1}/{num_questions}: {list(questions.keys())[i]}")
        print("Antwortmöglichkeiten: ")
        for answer in question["answers"]:
            print(answer)
        user_answer = input("Wie Lautet die richtige Antwort? (A, B, C oder D?) : ").lower()
        while True:
            if user_answer !="a" and user_answer !="b" and user_answer !="c" and user_answer !="d":
                print("Die korrekte Antwort muss einer der Möglichkeiten A, B, C oder D entsprechen")
                user_answer = input("Wie Lautet die richtige Antwort? (A, B, C oder D?) : ").lower()
            else:
                break
        if user_answer == question["correct_answer"]:
            print("Richtig")
            score += 1
        else:
            print("Falsch!")
            print("Die richtige Antwort wäre: "+question["correct_answer"])
        print("---------------------------------")
    print("Du hast alle Fragen beantworet!")
    print(f"Dein Ergebniss: {score}/{num_questions}")

#Diese Methode fügt das Hauptmenü ein von dem aus man Quizzes spielen und erstellen kann
def main_menu():
    while True:
        print("----------Hauptmenü----------\n1.Neues Quiz erstellen\n2.Erstellte Quizzes Spielen\n3.Quiz Löschen\n4.Spiel Verlassen")
        choose_mode = input("Auswahl :")
        match(choose_mode):
            case "1":
                create_quiz()
            case "2":
                play_quiz()
            case "3":
                delete_quiz()
            case "4":
                break
            case _:
                choose_mode = input("Ungültige Eingabe, bitte Antworten sie nur mit 1, 2, 3 oder 4! :")

main_menu()