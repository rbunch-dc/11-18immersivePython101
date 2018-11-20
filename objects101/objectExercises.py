class Person(object):
    def __init__(self, name, email, phone): # this is a constructor
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = [] #empty list of friends :(
        self.greeting_count = 0

    def greet(self, other_person):
        self.greeting_count += 1
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
    def print_contact_info(self):
        print '%s\'s email: %s, %s\'s phone: %s' % (self.name, self.email, self.name, self.phone)
    def add_friend(self,friend):
        self.friends.append(friend)
    def num_friends(self):
        return len(self.friends)

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
# Have sonny greet jordan using the greet method.
sonny.greet(jordan)
# Have jordan greet sonny using the greet method.
jordan.greet(sonny)
# Write a print statement to print the contact info (email and phone) of Sonny.
print sonny.email, sonny.phone
# sonny.print_info()
# Write another print statement to print the contact info of Jordan.
sonny.print_contact_info()
jordan.print_contact_info()

sonny.friends.append(jordan)
sonny.friends.append(jordan)
sonny.friends.append(sonny)
sonny.add_friend(sonny)

sonnysNumFriends = sonny.num_friends()
print sonny.num_friends()
print sonny.num_friends
sonny.num_friends()
print len(sonny.friends)

# primitives: integer, float, string, boolean
# 3 abstract data types:
# dictionary: diction['key']
diction = {
    "key":"value",
    "name":"joe",
    "phone":"222"
}
# list: aList[0]
aList = [
    "value",
    "joe",
    "222"
]
# object: sonny.name
# we define with the class keyword
# and then we Instantiate an object by calling the class
# classes have constructor functions (__init__), it's run
# on creation, and sets self variables
# objects use . notation
# the really big differeces between classes and dictionary:
# 1. classes have a schema
# 2. classes have methods


class Vehicle(object):
    # python will call this one when its supposed
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print self.year, self.make, self.model
    def __repr__(self):
        return "The make is: %s, the model is: %s %s" % (self.make,self.model,self.year)


car = Vehicle('Nissan', 'Leaf', 2015)
car2 = Vehicle('Ford', 'Focus', 2015)
# print car.make, car.model, car.year
car.print_info()
car2.print_info()

print car