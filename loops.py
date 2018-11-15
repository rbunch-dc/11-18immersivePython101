# Print a Triangle
# Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******

# Khanh, Brandon, Bryan
p = int(raw_input("How big is your triangle?!"))
p = p+1
for i in range(1,p,2):
    print "-"*p+i*"*"
    p -= 1


# Print a Triangle

# Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******

height = 4
for i in range(1,height+1):
	# print the padding (spaces)
	spaces = (height-i) * 2 * " "
	stars = ((i - 1) * 2 + 1) * "* "
	print ( spaces + stars ) 


def print_star():
	spaces = " " * (space_count / 2)
	stars = "*" * star_count
	print ( spaces + stars + spaces ) 
total_width = 10
star_count = 1
space_count = total_width - star_count
loop_count = 1
while loop_count <= 10:
	if(star_count % 2 == 1):
		print_star()
	star_count += 1
	space_count -=1
	loop_count += 1


# Bonus: Print a Banner

# Given a string, input by the user, print that string with a box around it. T
# he box should stretch to the length of the string. Example session:

# $ python banner.py
# Text? Welcome to DigitalCrafts
# ****************************
# * Welcome to DigitalCrafts *
# ****************************

input_text = "Good morning, Vietnam"
for i in input_text:
	print (len(input_text) * "*" + "**")
	print ("*" + input_text + "*")
	print (len(input_text) * "*" + "**")
	break
