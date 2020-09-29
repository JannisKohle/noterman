# noterman implementation in Python

import sys
import os
import json

def printUsage(): # and exit
    print("\nUsage:\nnoterman [--setup DIR | --list TAG | --add | --change ID | --delete ID]\n")
    exit()

argv = sys.argv

##########

def getDIR(): # get DIR from the config file
    if "noterman.json" in os.system("ls " + os.path.expanduser("~/.config")):
        with open(os.path.expanduser("~/.config/noterman.json"), "r+") as f:
            content = json.load(f)
            return content["DIR"]
    else:
        return 0

##########

if len(argv) == 1:
    printUsage()

elif argv[1] == "--help":
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
