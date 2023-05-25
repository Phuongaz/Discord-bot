import sys
import script_manager
import os

def __load__():
    script_manager.register_command("reload", "Reload bot", "reload")

async def execute(data, message, *args):
    await message.channel.send("Reloaing bot...")
    python = sys.executable
    os.execl(python, python, * sys.argv)