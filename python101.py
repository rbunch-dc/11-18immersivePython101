# print "Hello, World";
# print("Hello, World");

# print """
#     It was a dark and stormy night.
#     A murder happened.
# """

# print 'Hello, World'

# print 'Khanh "the man" Vu'
print 'Binga O\'Neil\n'

# # Variables
# # - strings, letters, numbers, or any other stuff 
# # you can make with a keyboard
# # a variable is just a fast way to refer to something else
# # variables do not make the program faster.
# # They make the program slower! 
# # Variables make it easier for us to write programs.

# # theBestClass = "the 11-18 immersive"
# # print theBestClass

# # Data Types
# # - Programming langauges see different types fo variables
# # differently
# # - String - English stuff.
# # - Number - I think you know what this is. Something with numbers (or - or e)
# # # print 3.3e10+"Joe"
# # -- float = it has a . in it
# # -- integer - has no .
# # - Booleans - true or false, on or off, 1 or 0, yes or no, right or left
# # - List - list of things. a single variable with a bunch of parts
# # - Dictionaries - variable of variables
# # - Objects - super dictionaries

# # Primitive Data tyes = string, number, boolean
# month = "November";
# print type(month)
# date = 13
# print type(date)
# dateAsFloat = 13.0
# print type(dateAsFloat)
# aBool = True
# print type(aBool)
# aList = []
# print type(aList)
# aDictionary = {}
# print type(aDictionary)

# # concatenate is programming speak for add things together
# first = "Robert"
# last = "Bunch"
# fullName = first + last;
# fullName = first + " " + last;
# print fullName

# fourteen = 10 + 4
# print fourteen
# fourteen = "10" + "4"
# print fourteen
# # fourteen = 10 + "4"
# # print fourteen

# # cast = change a variable to a new data type
# fourteen = int("10") + 4
# fourteen = int("ten") + 4

# Math = +, -, /, *, %
# print 2+2
# print 2-2
# print 2/2
# print 2*2
# # % = modulus. Moudulus divides the number and gives you the remainder
# print 2%2 
# print 2%3
# print 2**3
# print 10**87
# A string and a * and a number = give me X strings
# print "--" * 20
# print "Rob"**20+" The world already has too many Robs"

# Python does not have a simple incrementer
num = 1;
# num++
num += 1
# C
# C++

# Input
# Python 2 = raw_input
# Python 3 = input
# name = raw_input("What is your name? ")
# print type(name)

# conditionals
# a single = sign, means set the left to whateer is on the right
# two = signs, means compare what's on the left, to wahtever is on the right
print 2 == 2
print 2 == 1
print 2 == "2"
secret_number = 5;
if(secret_number == 3):
    print "Secret number is 3";
else:
    print "Secret number is not 3.";

game_on = True;
i = 0;
# while(game_on):
while(game_on == True):
    i+= 1
    if(i == 10):
        game_on = False
    else:
        print "Game on!!"
print "Loop exited!"