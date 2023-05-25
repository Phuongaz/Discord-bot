import discord
import script_manager
from config import *
from modules import module_manager
class MyClient(discord.Client):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged on as', self.user)
        await module_manager.load_modules(self)
        #await self.get_channel(CHANNEL_ID_GENERAL).send("Bot đã online!")
        
    async def on_message(self, message):
        try:
            if message.author == self.user:
                return
            cmd = message.content.split()[0]
            if cmd.startswith(COMMAND_PREFIX):
                commands = script_manager.get_all_command()
                cmd = cmd.replace(COMMAND_PREFIX, "")
                if cmd in commands:
                    await script_manager.invoke(cmd, self, message)
                    await self.react(message)
        except Exception as e:
            print("____________________________________________________")
            print(e)
            print("____________________________________________________")
            await self.react(message, "❌")
            await message.channel.send(f"{message.author.mention}! Lỗi CMNR...\nError: " + str(e))
            
    async def react(self, message, react = u"\U0001F44C"):
        await message.add_reaction(react)
        
if __name__ == '__main__':
    script_manager.load_scripts()
    print("Starting bot...")
    client = MyClient(intents=discord.Intents.all())
    client.run(TOKEN)