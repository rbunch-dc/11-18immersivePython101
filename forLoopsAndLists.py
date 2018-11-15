
# # A for loop expects a starting point, and an ending point
# # The ending point is non-inclusive, meaning it will stop 
# # when/BEFORE it gets there

# # i = the thing that will change each time through
# for i in range(1,10):
#     print i
#     # i += 1 -- unncessary

# # a 3rd argument you can hand, is called "step"
# # by default the step is 1
# for i in range(1,10,2):
#     print i

# # ============LISTS============ 
# # Lists = Arrays in any other language
# # a list is a list of variables
# student1 = "Brian"
# student2 = "Brandon"
# student3 = "Zac"
# student4 = "J.R."
# print student1
# print student2
# print student3
# print student4

# # A list groups "stuff" together and indexes them by number
# # A list index ALWAYS starts at 0
# # a list is made with []. 
# # when making a list, separate each index with a ,
# students = [
#     "Brian",
#     "Brandon",
#     "Zach",
#     "J.R."
# ]
# students = ["Brian","Brandon","Zach","J.R."]
# students[2] = "Zac"
# # print students[4] -- ERROR!!
# # print students[0] -- get the first element in the list
# # print students[-4]

# # All lists, have a length you can find with len()
# numOfStudents = len(students)
# for i in range(0,numOfStudents):
#     print "Welcome to class, %s" % students[i]

# # make a list called nflTeams
# teams = [
#     [
#         "Falcons",
#         "Panthers",
#         "Saints",
#         "Bucs",        
#     ],
#     "Bills",
#     "Dolphins",
#     "49ers",
# ]
# # print teams[0][0]

# # A Tuple is a list who's elements CANNOT be changed
# # A tuple is made with () instead of []
# students = ("Michael","Matt","Cody","ConnEr")
# students[3] = "Connor"

# Create an empty list
atlanta_teams = []
# to add something to the end of a list, 
# you can use the append
atlanta_teams.append("Falcons")
atlanta_teams.append("Braves")
atlanta_teams.append("Hawks")
atlanta_teams.append("Thrashers")

# Hey! Wait a minute, Rob... the Thrashers left years ago
# LISTNAME.pop() will remove the last element in a list
# LISTNAME.pop(3) will remove the 3th element in a list
atlanta_teams.pop()
print atlanta_teams
atlanta_teams.append("United")
# atlanta_teams.append(3)
# atlanta_teams.append(["Arthur Blank","Tom Wolfe"])
print atlanta_teams[1:3]

# A sort method for lists!
# atlanta_teams.sort()
# print atlanta_teams

# if you want to sort, but not change the oringal
# you can use sorted(LISTNAME)
sortedAtlantaTeams = sorted(atlanta_teams)
print atlanta_teams
print sortedAtlantaTeams

# reverseSort is the .resvers()
sortedAtlantaTeams.reverse()
print sortedAtlantaTeams

# If you have a string and want to turn it into a list...
# split!
reindeer = "Dasher, Dancer, Prancer, Vixon"
# split expects a delimiter. The delimiter is what you want
# split to look, and each time it finds it, it will create
# a new element.
reindeerAsAList = reindeer.split(", ")
print reindeerAsAList

# If you want part of a list, you use [x:y]
# this will create a COPY of the array. It will NOT change
# the original. It will start coppying at the Xth index
# and it will STOP at the Yth.
# So, if we wanted just Dancer, Prancer...
dancerPrancer = reindeerAsAList[1:3]
print dancerPrancer