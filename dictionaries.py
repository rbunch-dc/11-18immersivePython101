# DICTIONARIES
# Dictionaries are just like lists
# Except... instead of numbered indicies, they
# have English indicies

greg = [
    "Greg",
    "Male",
    "Tall",
    "Developer"
]
# If I wanted to know Greg's job, I have to do greg[3]
# No one is going to expect that

# A dictionary is like a list of variables
name = "Greg"
gender = "Male"
height = "Tall"
job = "Developer" 

# Key:value pair
greg = {
    "name": "Greg",
    "gender": "Male",
    "height": "Tall",
    "Job": "Developer"
}
# print greg["name"]
# print greg["Job"]

# Make a new dictionary
zombie = {} #dictionary
zombies = [] #list
# zombies.append()
zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed1'] = 10

print zombie
print zombie['weapon']

for key,value in zombie.items():
    print "Zombie has a key of %s with a value of %s" % (key, value)

# in our game, poor zombie loses his weapon (arm falls off)
# we need to remove his "weapon" key
del zombie['weapon']
print zombie
is_nighttime = True
if(is_nighttime):
    zombie['health'] += 50

# Put lists and dictionaries together!!!
zombies = []
zombies.append({
    'name': 'Hank',
    'weapon': 'baseball bat',
    'speed': 10
})
zombies.append({
    'name': 'Willie',
    'weapon': 'axe',
    'speed': 3,
    'victims': [
        'squirrel',
        'rabbit',
        'racoon'
    ]
})

# this will get the first zombie in zombies weapon
print zombies[0]['weapon'] 
# this will get the second victim, in the second zomnbies list of victims
print zombies[1]['victims'][1]

# if we wante to know, zombie1's weapon:
