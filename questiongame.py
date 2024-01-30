quiz_data = [
  {
      'question': "What is the capital of Poland?",
      'options': {'A': 'Krakow', 'B': 'Warsaw', 'C': 'Wroclaw', 'D': 'Lodz'},
      'answer': 'B'
  },
  {
      'question': "How many elements are in the periodic table?",
      'options': {'A': '116', 'B': '117', 'C': '118', 'D': '119'},
      'answer': 'C'
  },
  {
      'question': "How many countries are there in the European Union?",
      'options': {'A': '25', 'B': '26', 'C': '27', 'D': '28'},
      'answer':'C'
  },
  {   'question': "What is the most populous country in the world?",
      'options': {'A': 'India', 'B': 'Turkey', 'C': 'Poland', 'D': 'Argentina'},
      'answer':'A'
  },
  {   'question': "What operating system does Apple use?",
      'options': {'A': 'Linux', 'B': 'Android', 'C': 'IOS', 'D': 'Windows'},
      'answer':'C'
  },
  {
      'question': "Which is the German car?",
      'options': {'A': 'Honda', 'B': 'Mercedes-Benz', 'C': 'Dodge', 'D': 'Toyota'},
      'answer':'B'
  },
  {
      'question': "Which country won the last world cup?",
      'options': {'A': 'Argentina', 'B': 'Spain', 'C': 'Poland', 'D': 'France'},
      'answer':'A'
  },
  {
      'question': "Who is the player who has won the most Ballon D'or awards in history?",
      'options': {'A': 'Neymar', 'B': 'Lewandowski', 'C': 'C.Ronaldo', 'D': 'L.Messi'},
      'answer':'D'
  },
  {
      'question': "Which team won the last Champions League?",
      'options': {'A': 'Besiktas', 'B': 'M.City', 'C': 'Real Madrid', 'D': 'Bayern Munchen'},
      'answer':'B'
  },
  {
      'question': "What was the first programming language used?",
      'options': {'A': 'Java', 'B': 'Fortran', 'C': 'Python', 'D': 'C#'},
      'answer':'B'
  }
]

guesses = []
points = 0

class Quiz:
  def __init__(self, quiz_data):
      self.quiz_data = quiz_data
      self.guesses = []
      self.points = 0

  def start_quiz(self):
      print("Hello, welcome to my quiz!")
      print("Each question is worth 10 points")

      for question_data in self.quiz_data:
          print("-------------------")
          print(question_data['question'])
          for option, value in question_data['options'].items():
              print(f"{option}: {value}")

          guess = input("Enter (A, B, C, D): ").upper()
          self.guesses.append(guess)

          if guess == question_data['answer']:
              self.points += 10
              print("Correct!")
          else:
              print("Incorrect!")
              print(f"The correct answer is {question_data['answer']}")

      self.display_results()

  def display_results(self):
      print("-------------------")
      print("      RESULTS      ")
      print("-------------------")

      correct_answers = [question['answer'] for question in self.quiz_data]
      print("Answers:", " ".join(correct_answers))
      print("Guesses:", " ".join(self.guesses))
      print(f"Your score is: {self.points}/{len(self.quiz_data) * 10} ({self.points}%)")


quiz_instance = Quiz(quiz_data)
quiz_instance.start_quiz()
