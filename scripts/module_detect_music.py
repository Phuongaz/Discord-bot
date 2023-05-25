import script_manager
from modules import detect_music
import discord 
from config import *
def __load__():
    script_manager.register_command("dtmusic", "Tra tên bài hát bằng lời", "detect_music")

async def execute(data, message, *args):
    if args[0] is not None:
        lyric = message.content.replace(COMMAND_PREFIX + "dtmusic", "").strip()
        title = detect_music.detect_music(lyric)
        embed = discord.Embed(title="Tra tên bài hát bằng lời", description=title, color=0x00ff00)
        await message.channel.send(embed=embed)