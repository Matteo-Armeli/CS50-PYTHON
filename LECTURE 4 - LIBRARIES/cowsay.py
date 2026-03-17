#introducing packages: modules implemented to a folder (3rd party libraries) 
#pypi.org/project/cowsay
#pip package manager allows you to install new libraries

import cowsay
import sys

#usiamo il + perché non puoi fare , con questa funzione
if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

#.trex
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])