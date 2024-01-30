quiz_data = {
    "questions": [
        "What is the capital of Poland?",
        "How many elements are in the periodic table?",
        "How many countries are there in the European Union?",
        "What is the most populous country in the world?",
        "What operating system does Apple use?",
        "Which is the German car?",
        "Which country won the last world cup?",
        "Who is the player who has won the most Ballon D'or awards in history?",
        "Which team won the last Champions League?",
        "What was the first programming language used?"
    ],
    "options": [
        ["A: Krakow", "B: Warsaw", "C: Wroclaw", "D: Lodz"],
        ["A: 116", "B: 117", "C: 118", "D: 119"],
        ["A: 25", "B: 26", "C: 27", "D: 28"],
        ["A: India", "B: Turkey", "C: China", "D: Pakistan"],
        ["A: Linux", "B: Windows", "C: iOS", "D: Android"],
        ["A: Nissan", "B: Lamborghini", "C: Mercedes-Benz", "D: Honda"],
        ["A: Spain", "B: Argentina", "C: Portugal", "D: France"],
        ["A: C.Ronaldo", "B: L.Messi", "C: Mbappe", "D: R.Lewandowski"],
        ["A: Real Madrid", "B: Barcelona", "C: Manchester City", "D: Besiktas"],
        ["A: Python", "B: Fortran", "C: Java", "D: C#"]
    ],
    "answers": ["B", "C", "C", "A", "C", "C", "B", "B", "C", "B"]
}

guesses = []
points = 0

print("Hello, welcome to my quiz!")
print("Each question is worth 10 points")

for question, options in zip(quiz_data["questions"], quiz_data["options"]):
    print("-------------------")
    print(question)
    for option in options:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == quiz_data["answers"][len(guesses) - 1]:
        points += 10
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {quiz_data['answers'][len(guesses) - 1]}")

print("-------------------")
print("      RESULTS      ")
print("-------------------")

print("Answers:", " ".join(quiz_data["answers"]))
print("Guesses:", " ".join(guesses))
print(f"Your score is: {points}/{len(quiz_data['questions']) * 10} ({points}%)")
