import script_manager

def __load__():
    script_manager.register_command("stop", "Stop command", "stop")

async def execute(data, message, *args):
    await message.channel.send("Stopping bot...")
    exit()