import random  
# We need random to let the computer pick a secret number 
#random.randint(1, 100) gives a random integer between 1 and 100 (inclusive)



secret = random.randint(1, 15)   
#secret holds the number the player must guess.
#Every time you run the program, it's different.



attempts = 0
#👉 Counts how many guesses the player makes.
#Starts at 0.


max_attempts = 5
#set the maximum number of attempts to 3




while attempts < max_attempts:  
    #runs only while attempts < 3

    guess = int(input(f" Attempts {attempts + 1}/{max_attempts} - Guess a number between 1 and 10: "))

    attempts += 1
    # Every guess counts as one attempt

    if guess < secret:
        print ("Too low!")

    elif guess > secret:
        print ("Too high!")

    else:
        print ("🎉 Correct! You guessed it in {attempts} attempts.")
        break
else:
    print (f"❌ Out of attempts! The number was {secret}")

    