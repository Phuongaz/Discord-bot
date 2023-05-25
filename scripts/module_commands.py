import script_manager
import discord
from config import *
def __load__():
    script_manager.register_command("commands", "Xem tất cả lệnh", "commands")

async def execute(data, message, *args):
    embed = discord.Embed(title="CÁC LỆNH HIỆN TẠI!")
    for command in script_manager.get_all_command():
        embed.add_field(name= COMMAND_PREFIX + command , value=script_manager.get_description(command), inline=False)
    await message.channel.send(embed=embed)