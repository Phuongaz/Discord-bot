Simple discord bot for locm server [WIP]


P/S: Go to ```config.py``` to setup your bot

# CREATE A COMMAND SCRIPT
- `Step 1:` go to scripts folder and create a file start with `module_`
- `Step 2:` import your code!

# EXAMPLE COMMAND SCRIPT
```module_command.py```
```python
import script_manager

#required function
def __load__(): 
    # register command (command name, description, modules_name)
    script_manager.register_command("command_0", "description", "command") 

#function will be executed
async def execute(data, message, *args):
    await message.channel.send("Hello world!")
```
