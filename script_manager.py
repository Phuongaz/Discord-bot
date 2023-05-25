import importlib
import os
import sys

command_prefix = "[Command]"
script_prefix = "[SCRIPT]"
dict_commands = {}

def register_command(command, description, module):

    if command in dict_commands:
        print(command_prefix + " '" + command + "' has been registered!")
    else:
        dict_commands[command] = {"description" : description, "module": module}
        print(command_prefix +" Register command: " + command + " (" + description + ")")

def get_all_command():
    return dict_commands

def get_description(command) -> str:
    return dict_commands[command]["description"]

def exist_command(command):
    return command in get_all_command

def get_module(command):
    return dict_commands[command]["module"]

async def invoke(command, data, message):
    sys.path.append("scripts")
    call = importlib.__import__("module_%s" % get_module(command))
    args = message.content.split(" ")
    await call.execute(data, message, args[1:])

def load_scripts():
    sys.path.append("scripts")
    current_path = os.path.dirname(os.path.abspath(__file__))+ "\\scripts"
    i = 0
    for file in os.listdir(current_path):
        if("module_" in file):
            print(script_prefix + " Loaded script " + file)
            sys.path.append("scripts")
            script = importlib.__import__(file.split(".py")[0])
            script.__load__()
            i += 1
    print(script_prefix + " loaded " + str(i) + " scripts")