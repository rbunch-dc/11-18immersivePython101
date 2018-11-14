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
        print "Great job. Game over."
    # If the user did not guess teh right number, tell them
    # to guess again
    else:
        print "Guess again..."