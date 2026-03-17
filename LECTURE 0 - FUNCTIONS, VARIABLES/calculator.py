# + - * / % supported symbols (and more) 
# % sign is not percentage but a "modulo operator" that takes a remainder after dividing a number by another

# Let's say x=1 and y=2
x=input("What's x? ")
y=input("What's y? ")

# Actual problem is + sign is used to concatenate and not to add as numbers
z = x + y

# So this will print 12 and not 3 as expected
print(z)

x=input("What's x? ")
y=input("What's y? ")

# Here's how to fix with int (integers), now they will add
z = int(x) + int(y)

print(z)

# Do I really need z variable? Not if I nest

x = int(input("What's x? "))
y = int(input("What's y? "))

# Since every string is integer now, they will add
print(x+y)

# Even more nests if you prefer, but readability looks bad and could lead to mistakes
print(int(input("What's x? ")) + int(input("What's y? ")))

# If the numbers are not gonna be int but instead they are gonna be float like 1.2 or 3.4
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x+y)

# If we want the answer to be rounded to the nearest int
"""round(number[, ndigits])"""

# So now...
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y)

print(z)

# If x=999, y=1, so z=1000, how to Format the number with a ./, and you have a 1.000/1,000?
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y)

print(f"{z:.}")

# Floats cannot represent number infinite precisely, they have a cap.

x = float(input("What's x? "))
y = float(input("What's y? "))

# Adding ",2" will round in 2 digits so it will print 0.67 instead of 0.6666666666666666
z = round(x/y,2)

print(z)

# Alternative way if I don't want to use the round function, I can use a format string
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x/y

print(f"{z:.2f}")

# Now I want it to Return Values
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n #or n**2 or pow(n, 2)

main()