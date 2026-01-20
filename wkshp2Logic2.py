import random
secret_number = random.randint(1, 10)  
guess = int(input("Guess the number I'm thinking of between 1 and 10: "))
if guess > secret_number:
    print("Too high! The secret number was ", secret_number)
elif guess < secret_number:
    print("Too low! The secret number was ", secret_number)
else:
    print("You got it! The secret number was ", secret_number)