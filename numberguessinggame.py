import random
rand_num = random.randint(1,100)
guess = 0
user_level = input("Choose a level 'easy' or 'hard' ").lower()
if(user_level == "easy"):
    guess = 10
    print("You have 10 chances to guess the number")
elif(user_level == "hard"):
    guess = 5
    print("You have 5 chances to guess the number")
else:
    print("Choose a appropriate choice")
while guess > 0:
    user_guess = int(input("Make a Guess:"))
    if(user_guess == rand_num):
        is_won = True
        break
    elif(user_guess > rand_num):
        print("Too High")
        guess -=1
        print(f"You have {guess} chances left")
    elif(user_guess < rand_num):
        print("Too Low")
        guess -=1
        print(f"You have {guess} chances left")
if(is_won):
    print("You guessed it right!!")
else:
    print("Game over")
    print(f"The number was {rand_num}")