import random

highest = 10
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and 10: ")

while True:
    guess = int(input())
    
    if guess == 0:
        break
    elif guess < answer:
        print("Please guess higher:")
    elif guess > answer:
        print("Please guess lower:")
    else:
        print("You got it")
        break