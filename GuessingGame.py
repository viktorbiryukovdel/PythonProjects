import random

print("Set the range of numbers in which you would like to guess:")
number = int(input())
random_number = random.randint(1, number)

print("Now, guess the number between 1 and", number)
guess = 0
while guess != random_number:
  print("Guess the number now:")
  guess = int(input())
  if guess > random_number:
    print("Your number is too high!")
  elif guess < random_number:
    print("Your number is too low")
  else:
    print("You are spot on!")
