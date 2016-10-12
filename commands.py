import os

def help():
    response = "Commands\n--------------------\n"
    response += "add <name> : adds an intern\n"
    return response
# command: add <name>
# example: add jbtyson
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

# command: update <add|clear> <section> <text>
# example: update add yesterday testing testing 1 to 3
def update(command):
    args = command.split(' ', 4)
    name = args[1]
    filename = name["data/" + name + ".txt"]
    if not os.path.isfile(filename):
        return error("update", "Intern named: " + name + " - does not exist.")

    action = args[2]
    if action == "add":
        if len(args) < 4:
            return error("update", "Invalid argument syntax, message parameter expected.")
        message = args[3]
    elif action == "clear":
        if len(args) == 3:
            with open(filename, "w"):
                pass
    else:
        return error("update", "Invalid action parameter provided.")

    section = args[3]
    if section == "yesterday":
        return None
    elif section == "today":
        return None
    elif section == "challenges":
        return None
    else:
        return None

def error(commandName, errorMessage):
    if commandName == "update":
        message = "Error: " + errorMessage + "\nProper Usage: update <add|clear> <section> <text>"
    return message
