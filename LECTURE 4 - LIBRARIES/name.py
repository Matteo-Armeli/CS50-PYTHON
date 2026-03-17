#sys.argv argument vector
import sys

try:
    print("Hello, my name is", sys.argv[1])

#to clarify the index error and not let it be cryptik
except IndexError:
    print("Too few arguments")

#another version
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


#sys.exit to be sure to exit earlier
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

    print("hello, my name is", sys.argv[1])

#I don't want to limit the number of prompts
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)

#introducing slices [1:] and you can use [-1:] for the other part of list
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)