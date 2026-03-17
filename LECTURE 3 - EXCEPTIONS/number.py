#Exceptions: "try" and "except" for handling errors
try:
    x = int(input("What's X? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

#Introducing name error
try:
    x = int(input("What's X? "))
except ValueError:
    print("x is not an integer")
#fixed by else:
else:
    print(f"x is {x}")

#Introducing loops to prompt until user cooperate with inputting integer
while True:
    try:
        x = int(input("What's X? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

#proposing to define a function
def main():
    x = get_int()
    print(f"x is {x}")

#return is stronger than break and returns+breaks
def get_int():
    while True:
        try:
            x = int(input("What's X? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
main()

#variation
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's X? "))
        except ValueError:
            print("x is not an integer")
main()

#pass to silently ignore
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's X? "))
        except ValueError:
            pass
main()

#dynamics for reusable code
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()

#raise exception using "raise" key...