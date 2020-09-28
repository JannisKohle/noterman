# noterman implementation in Python

import sys
import os

def printUsage(): # and exit
    print("\nUsage:\nnoterman [--setup DIR | --list TAG | --add | --change ID | --delete ID]\n")
    exit()

argv = sys.argv

##########

if len(argv) == 1:
    printUsage()

elif argv[1] == "--setup":
    if len(argv) == 2: # --setup (Create config file, if it exists already - check DIR setup)
        pass

    elif len(argv) == 3: # --setup DIR (Create config file and setup DIR)
        pass

    else:
        printUsage()

elif argv[1] == "--list":
    if len(argv) == 2: # --list (List all)
        pass

    elif len(argv) == 3: # --list TAG (List all with TAG)
        pass

    else:
        printUsage()

elif argv[1] == "--add":
    if len(argv) == 2: # --add (add note with RANDOM id)
        pass

    else:
        printUsage()

elif argv[1] == "--change":
    if len(argv) == 3: # --change ID
        pass

    else:
        printUsage()

elif argv[1] == "--delete":
    if len(argv) == 3: # --delete ID
        pass

    else:
        printUsage()

else:
    printUsage()
