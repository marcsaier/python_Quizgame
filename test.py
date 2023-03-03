#Hier werden Dinge ausprobiert...
#Optimal bin ich leer...

questions = {}

def insert_questions():
    question = input("Wie lautet die Frage? :")
    correct_answer = input("Wie ist die korrekte Antwort für die Frage? :")
    answers = ["A: "+input("Füllen sie die 4 Antwortmöglichkeiten aus:\nA =:"),
               "B: "+input("B =:"),
               "C: "+input("C =:"),
               "D: "+input("D =:")]
    questions[question] = {"correct_answer": correct_answer, "answers": answers}

insert_questions()
insert_questions()

first_question = questions[list(questions.keys())[0]]
print("Frage: " + list(questions.keys())[0])
print("Antwortmöglichkeiten: " + str(first_question["answers"]))