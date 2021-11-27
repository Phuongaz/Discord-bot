import script_manager
import discord
def __load__():
    script_manager.register_command("commands", "Xem tất cả lệnh", "commands")

async def execute(data, message, *args):
    embed = discord.Embed(title="CÁC LỆNH HIỆN TẠI!")
    for command in script_manager.get_all_command():
        embed.add_field(name=command , value=script_manager.get_description(command), inline=True)
    await message.channel.send(embed=embed)