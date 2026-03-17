#building vertical obstacle in super mario bros
print("#")
print("#")
print("#")

#integration of what we learned
for _ in range(3):
    print("#")

#better version with def
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
main()

#clever version
def print_column(height):
    print("#\n" * height, end="")
main()

#building horizontal boxes in super mario bros
def main():
    print_row(4)

def print_row(width):
    print ("?" * width)
main()

#building the barriers in the puzzle vulcano castle
def main():
    print_square(3)

def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):
        
            #print brick
            print("#", end="")

        print()  
main()

#more optimizations
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)
main()

#More clarity on what we did with print("#" * size)
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)      
main()