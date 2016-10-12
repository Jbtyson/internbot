import os

def add(command):
    name = command.split( )[1]
    fileName = "data/" + name + ".txt"
    if os.path.isfile(fileName):
        response = name + " is already added."
    else:
        f = open(fileName, "a+")
        f.close()
        response = name + " was added."
    return response;
