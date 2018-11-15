# Uppercase a String
# Given a string, print the string uppercased. #string #easy
aString = "connor";
# aStringAsUpper = aString.upper()
# print aString

# Capitalize a String
# Given a string, print the string capitalized. #string #easy
# print aString.capitalize()

# Reverse a String
# Given a string, print the string reversed.
# print aString[::-1]
# ------
# print aString.reverse()
# aStringAsList = list(aString)
# print aStringAsList
# aStringAsList.reverse()
# print aStringAsList
# print ''.join(aStringAsList)

# print aString[0]

lengthOfString = len(aString)
# print lengthOfString
reversedString = ""
for i in range(0,lengthOfString):
    reversedString += aString[lengthOfString-(i+1)]
print reversedString

# Leetspeak
# Given a paragraph of text as a string, print the paragraph in leetspeak. 
# To translate a string to leetspeak, you need to replace make the 
# following character replacements (treat all input 
# characters as uppercase):

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7
# Example: Leet => l337

leetString = "Sean McQuaid"
newString = leetString.upper()
leetA = newString.replace("A","4")
leetE = leetA.replace("E","3")
leetG = leetE.replace("G","6").replace("I","1").replace("O","0").replace("S","7")

