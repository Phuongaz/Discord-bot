import script_manager

def __load__():
    #register_command(command, description, module)
    script_manager.register_command("test", "test command", "test")

async def execute(data, message, *args):
    await message.channel.send('Test script !!!!!')