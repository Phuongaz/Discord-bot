import discord
import script_manager
from config import *

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        cmd = message.content.split()[0]
        if cmd.startswith(COMMAND_PREFIX):
            commands = script_manager.get_all_command()
            cmd = cmd.replace(COMMAND_PREFIX, "")
            if cmd in commands:
                await script_manager.invoke(cmd, self, message)

if __name__ == '__main__':
    script_manager.load_scripts()
    print("Enable bot.....")
    client = MyClient()
    client.run(TOKEN)