# Definitions
""" 
Functions: input/print
Arguments: ("what's your name? ")/(f"hello, {name}")
Side effect: asks user's name / returns a message + what user will input as name 
"""

# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello, ", end="")
print(name)

"""All the in between is a comment and just as for # it will not be shown as for #text"""

# This one below is not just a str (string), these are parameters for the default behaviour
""" print(*objects, sep=' ', end='\n', file=None, flush=False)"""

# What if I want to print "quotes"? Use '' instead of ""
print('hello, "friend"')
# or \ for escape
print("hello, \"friend\"")

# Most elegant way to do that with f (format) string
name = input("What is your name? ")
print(f"hello, {name}")

# Remove whitespace from str (only left or right, not in between)
name = name.strip()

# Capitalize user's name - but will capitalize only the very first letter
name = name.capitalize()

# Capitalize user's name - every first letter of every word
name = name.title()

# Both can be chained in one line
name = name.strip().title()

# Or even better
name = input("What's your name? ").strip().title()
# Split user's name into first name and last name in case they input both
first, last = name.split(" ")
print(f"hello, {first}")

"""Some may prefer to detatch .strip().title() for personal preferences/readability"""

# Def (define) to create your new function, press tab to indent what the new def should do
def hello(to):
    print("hello,", to)

# Replace print(name) directly with hello(name)
name = input("What's your name? ")
hello(name)

# To say hello to someone generic, example: "hello world" and then ask user's name 
# Give parameters default value like with print(*objects, sep=' ', end='\n', file=None, flush=False)

def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)

# Always define custom functions at the very top with main() and remember to call main() in the end

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
# Could not do print("hello,", name) because name is now in main. This is called Scope.
    print("hello,", to)

main()