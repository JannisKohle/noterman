# noterman implementation in Python

import sys
import os
import json
import random

def printUsage(): # and exit
    print("\nUsage:\nnoterman [--setup DIR | --list TAG | --add | --change ID | --delete ID]\n")
    exit()

argv = sys.argv

##########

def getDIR(): # get DIR from the config file and return it WITHOUT '/' at the end
    if "noterman.json" in os.system("ls " + os.path.expanduser("~/.config")):
        with open(os.path.expanduser("~/.config/noterman.json"), "r+") as f:
            content = json.load(f)
            DIR = os.path.expanduser(content["DIR"])
            return DIR[:-1] if DIR.endswith("/") else DIR
    else:
        return 0

##########

if len(argv) == 1:
    printUsage()

elif argv[1] == "--help":
    printUsage()

elif argv[1] == "--setup":
    if len(argv) == 2: # --setup (Check DIR setup)
        DIR = getDIR()
        if DIR != 0:
            print("noterman will save your notes in " + DIR)
            exit()
        else:
            print("You haven't specified a directory for saving notes yet. You can\ndo that with 'noterman --setup DIR' where DIR is the directory.")
            exit()

    elif len(argv) == 3: # --setup DIR (Create config file and setup DIR)
        DIR = os.path.expanduser(argv[2])
        if not os.path.isdir(DIR):
            os.system("mkdir " + DIR)

        # create & write config file:
        if "noterman.json" not in os.system("ls " + os.path.expanduser("~/.config")): # create config file if it doesn't exist
            os.system(f"touch {~/.config}/noterman.json")

        with open(os.path.expanduser("~/.config/noterman.json"), "r+") as f:
            f.truncate(0) # clear file
            json.dump({"DIR": DIR}, f)

    else:
        printUsage()

elif argv[1] == "--list":
    if len(argv) == 2: # --list (List all)
        files = os.listdir(getDIR())
        print("{:>5}  {:12}  {:12}  {:10}\n".format("ID", "TAG", "TEXT", "DD/MM/YYYY"))
        for file in files:
            with open(getDIR()+"/"+file, "r+") as f:
                content = json.load()
            print("{:>5}  {:12}  {:12}  {:10}\n".format(content["id"], content["tag"], content["text"], content["date"]))

        print()
        exit()

    elif len(argv) == 3: # --list TAG (List all with TAG)
        files = os.listdir(getDIR())
        print("{:>5}  {:12}  {:12}  {:10}\n".format("ID", "TAG", "TEXT", "DD/MM/YYYY"))
        for file in files:
            with open(getDIR()+"/"+file, "r+") as f:
                content = json.load()
            if content["tag"] == argv[2]:
                print("{:>5}  {:12}  {:12}  {:10}\n".format(content["id"], content["tag"], content["text"], content["date"]))

        
        print()
        exit()

    else:
        printUsage()

elif argv[1] == "--add":
    if len(argv) == 2: # --add (add note with RANDOM id)
        text = input("text: ")
        tag = input("tag: ")

        id = random.randint(100, 999)
        date = "06/10/2020" # TODO

        DIR = getDIR()
        os.system(f"touch {DIR}/{id}.json")
        with open(f"{DIR}/{id}.json", "r+") as f:
            towrite = {"id": id, "text": text, "tag": tag, "date": date}
            json.dump(towrite, f)

    else:
        printUsage()

elif argv[1] == "--change":
    if len(argv) == 3: # --change ID
        newText = input("text: ")
        newTag = input("tag: ")

        id = argv[2]
        if id+".json" in os.listdir(getDIR()): # check if note exists
            with open(f"{DIR}/{id}.json", "r+") as f:
                content = json.load(f)
                content["text"] = text
                content["tag"] = tag
                f.truncate(0)
                json.dump(content, f)
            print(f"Successfully changed note #{id}")

        else:
            print(f"Note with id {id} does not exist.")

    else:
        printUsage()

elif argv[1] == "--delete":
    if len(argv) == 3: # --delete ID
        pass

    else:
        printUsage()

else:
    printUsage()
