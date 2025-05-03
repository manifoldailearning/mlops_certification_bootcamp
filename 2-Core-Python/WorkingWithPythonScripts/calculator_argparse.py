import argparse

# step 1: create a parser object
parser = argparse.ArgumentParser(description="Greet the user")

# step 2: add arguments to the parser --> inputs that is being passed to the script
parser.add_argument("x", help="enter the value of x",type=int)
parser.add_argument("y", help="enter the value of y", type=int) # optional argument
# add more arguments to the parser

# step 3: parse the arguments
args = parser.parse_args()
x = args.x
y = args.y
# step 4: use the arguments
s = x+y
print("The sum of the two numbers is:", s)