#Number Guessing Game Objectives:

import art
import random


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def check_answer(guess, answer, attempts):
  if guess > answer:
    print("Too high.")
    return attempts - 1
  elif guess < answer:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {answer}!")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': " )
  if difficulty == "easy":
    return EASY_LEVEL_ATTEMPTS
  elif difficulty == "hard":
    return HARD_LEVEL_ATTEMPTS


print(art.logo)

def game():

  print("Welcome to the Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  answer = random.randint(1, 100)

  attempts = set_difficulty()

  guess = 0

  while guess != answer:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, answer, attempts)
    if attempts == 0:
      print("You have ran out of attempts, you lose.")
      return
game()


