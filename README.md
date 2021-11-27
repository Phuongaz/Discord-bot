Simple discord bot for locm server [WIP]


P/S: Go to ```config.py``` to paste your token

# CREATE A COMMAND SCRIPT
- `Step 1:` go to scripts folder and create a file start with `module_`
- `Step 2:` import your code!

# EXAMPLE COMMAND SCRIPT
```module_command.py```
```python
import script_manager

#required function
def __load__(): 
    #
    script_manager.register_command("command_0", "description", "command") 
    script_manager.register_command("command_1", "description", "command") 

#function will be executed
async def execute(data, message, *args):
    if args[0][0] == "command_0":
        await message.channel.send('Test command')
    if args[0][0] == "command_1":
        await message.channel.send('Test command 1')
```
