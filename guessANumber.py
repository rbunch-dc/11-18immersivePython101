# import any needed modules
import random

# Ask the user for his or her name...
userName = raw_input("What is your name? ")

# Set up the (not-so) secret number as 5.
# secret_number = 5

# Generate a random number using the random module which is part of python
secret_number = random.randint(1, 10)
print secret_number

# Init the bool gameOn to True
gameOn = True
# Init a number of guesses
allowedGuesses = 5
# init userGuesses 
userGuesses = 0

# Run a loop until gameOn = False
while(gameOn):
    # get the users Input and store it in userGuess
    userGuess = raw_input("Guess a number between 1 and 10 ")    
    # if the userGuess = the secret number, then... 
    # change goneOn = False
    # single = means assignment, == compare
    # convert the user guess into a number
    userGuessAsInt = int(userGuess)

    # the user just made a guess. Count it
    userGuesses += 1


    if(userGuessAsInt == secret_number):
        # the user guessed the right number (or we wouldnt Run
        # this code) so change gameOn to false, so we can
        # quit the loop
        gameOn = False
        # Congratulate the user for being awesome!!
        print "Great job, %s. Game over." % userName
    # If the user did not guess teh right number, tell them
    # to guess again
    else:
        if(userGuesses == allowedGuesses):
            # User was wrong.
            # User has used up all their guesses.
            # game over.
            gameOn = False
            print "You are out of guesses! The number was %i" % secret_number
        # if the user is too high, tell them
        elif(userGuessAsInt > secret_number):
            # print "Your guess is too high"
            # print str(userGuessAsInt) + " is too high"
            print "%i is too high" % userGuessAsInt
            print "You have %i guesses left!" % (allowedGuesses-userGuesses)
        # if the user guess isn't too high, and it's not right
        # then it must be... to low
        else:
            # print "Your guess is too low"
            # option 1. print userGuess + " is too low"            
            # option 2. print str(userGuessAsInt) + " is too low"            
            # Interpolation = mixing strings and variables
            # In Python, you can interpolate with a % sign
            print "%s, %i is too low" % (userName,userGuessAsInt)
            print "You have %i guesses left!" % (allowedGuesses-userGuesses)

            print "Guess again..."
# import this


# If number = guess
# else
#     if number is too high
#     if number is too low

# if number is too high
# if number is too low
# if number is right


# while((gameOn) and (userGuesses < allowedGuesses)):