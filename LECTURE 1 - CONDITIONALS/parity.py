#% is the Modulo Operator and tells me the remainder (4:3=1 with a remainder of 1) è il resto in italiano
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Further with Bool (Boolean Valor can only be True or False)
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

#Improving the design now, in Pythonic (only in Python)
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

#We're using Boolean so no need to ask, just go with:
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0
