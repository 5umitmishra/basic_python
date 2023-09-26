import random
logo = """ _____                  _____                      _   _     _              
|_   _|                /  ___|                    | | | |   (_)             
  | |_   _ _ __   ___  \ `--.  ___  _ __ ___   ___| |_| |__  _ _ __   __ _  
  | | | | | '_ \ / _ \  `--. \/ _ \| '_ ` _ \ / _ \ __| '_ \| | '_ \ / _` | 
  | | |_| | |_) |  __/ /\__/ / (_) | | | | | |  __/ |_| | | | | | | | (_| | 
  \_/\__, | .__/ \___| \____/ \___/|_| |_| |_|\___|\__|_| |_|_|_| |_|\__, | 
      __/ | |                                                         __/ | 
     |___/|_|                                                        |___/  
     """

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

