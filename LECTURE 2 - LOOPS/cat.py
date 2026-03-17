print("meow")
print("meow")
print("meow")

#Introducing loops

i = 3
while i !=0: 
    print("meow")
    i = i -1

#Incremental and special syntax
i = 0
while i < 3:
    print("meow")
    i += 1

#For loop with list
for o in [0, 1, 2]:
    print("meow")

#Or and i is replaced by _ (generic variable)
for _ in range (3):
    print("meow")

#More pythonic things (less readable tho)
print ("meow\n" * 3, end="")

#Asking user how much creating an infinite loop and breaking it
while True:
    n = int(input("What's n? "))
    if n > 0:
       break
       
for _ in range(n):
    print("meow")

#defining
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()