# Ask the user for his or her name...
userName = raw_input("What is your name? ")

# Set up the (not-so) secret number as 5.
secret_number = 5
# Init the bool gameOn to True
gameOn = True
# Run a loop until gameOn = False
while(gameOn):
    # get the users Input and store it in userGuess
    userGuess = raw_input("Guess a number between 1 and 10 ")
    userGuessAsInt = int(userGuess)
    # if the userGuess = the secret number, then... 
    # change goneOn = False
    # single = means assignment, == compare

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
        # if the user is too high, tell them
        if(userGuessAsInt > secret_number):
            # print "Your guess is too high"
            print "%i  is too high" % userGuessAsInt
        # if the user guess isn't too high, and it's not right
        # then it must be... to low
        else:
            # print "Your guess is too low"
            # option 1. print userGuess + " is too low"            
            # option 2. print str(userGuessAsInt) + " is too low"            
            # Interpolation = mixing strings and variables
            # In Python, you can interpolate with a % sign
            print "%s, %i is too low" % (userName,userGuessAsInt)

            print "Guess again..."
# import this


# If number = guess
# else
#     if number is too high
#     if number is too low

# if number is too high
# if number is too low
# if number is right
