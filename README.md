# noterman

noterman is a command line interface for quickly writing & checking small notes **(MacOS only)**.
I'm planing to implement this in Python, and in C.

## What noterman can do:

With noterman, you can create, change and delete notes. Every note has a uid which
is used for deleting and changing notes.These notes can have tags, like ```school```
and ```programming```.

## Usage:

Before you can use noterman, you need to run ```noterman --setup DIR``` where DIR
is the directory for saving your notes. If you're using MacOS, i'd recommend
using ```~/Library/Application\ Support/noterman```.

- Create a new note: ```noterman --add```
- Change a note: ```noterman --change 438```
- Delete a note: ```noterman --delete 196```
- List all notes: ```noterman --list```
