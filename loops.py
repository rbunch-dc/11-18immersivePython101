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