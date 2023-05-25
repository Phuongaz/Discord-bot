import script_manager

def __load__():
    script_manager.register_command("description", "Description command", "des")

async def execute(data, message, *args):
    if args[0] is not None:
        des = script_manager.get_description(args[0])
        await message.channel.send('Command (' + args[0] + "): " + des)
        return
    await message.channel.send('Command not found')