import argparse

# step 1: create a parser object
parser = argparse.ArgumentParser(description="Greet the user")

# step 2: add arguments to the parser --> inputs that is being passed to the script
parser.add_argument("name", help="The name of the user")
parser.add_argument("--age", help="The age of the user", type=int) # optional argument
# add more arguments to the parser
parser.add_argument("--city", help="The city of the user", type=str)
x = 20
# step 3: parse the arguments
args = parser.parse_args()

# step 4: use the arguments
print("Hello", args.name)
if args.age:
    print("You are", args.age, "years old")
else:
    print("I dont know your age") 

print("You are from", args.city)
# run the script: python demo_argparase.py John --age 25

# run the script: python demo_argparase.py John



# run the script: python demo_argparase.py John --age 25 --city New York

# run the script: python demo_argparase.py John --age 25 --city New York
