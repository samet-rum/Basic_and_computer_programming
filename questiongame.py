questions = ("What is the capital of the poland?: ",
             "How many elements are in the periodic table?: ",
             "How many countries are there in the European Union?: ",
             "What is the most populous country in the world?: ",
             "What operating system does apple use?: ",
             "Which is the German car?: ",
             "Which country won the last world cup?: ",
             "Who is the player who has won the most Ballon D'or awards in history?: ",
             "Which team won the last Champions League?: ",
             "What was the first programming language used?: ",)

options = (("A: Krakow", "B: Warsaw", "C: Wroclaw", "D: Lodz"),
           ("A: 116", "B: 117", "C: 118", "D: 119"),
           ("A: 25", "B: 26", "C: 27", "D: 28"),
           ("A: India", "B: Turkey", "C: China", "D: Pakistan"),
           ("A: Linux", "B: Windows", "C: IOS", "D: Android"),
           ("A: Nissan", "B: Lamborghini", "C: Mercedes-Benz", "D: Honda"),
           ("A: Spain", "B: Argentina", "C: Portugal", "D: France"),
           ("A: C.Ronaldo", "B: L.Messi", "C: Mbappe", "D: R.Lewandowski"),
           ("A: Real Madrid", "B: Barcelona", "C: Manchester City", "D: Besiktas"),
           ("A: Python", "B: Fortran", "C: Java", "D: C#"))

answers = ("B", "C", "C", "A", "C", "C", "B", "B", "C", "B")
guesses = []
points = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D,): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        points += 10
        print("Correct!")
    else:
        print("Incorrect!")
        print("{} the correct answer".format(answers[question_num]))
    
    question_num += 1

print("-------------------")
print("      RESULTS      ")
print("-------------------")

print("answer: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

points = int(points)
print(f"Your points is {points}%") 
