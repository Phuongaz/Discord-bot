import discord
import script_manager
from config import *
from modules import watch_point
from util import number
def __load__():
    script_manager.register_command("wpoint", "Xem diem thi", "wpoint")

async def execute(data, message, *args):
    points = watch_point.listen_portal()
    embed = discord.Embed(title="DANH SÁCH ĐIỂM THI")
    embed.add_field(name="Tên sinh viên", value=points["ten_sv"], inline=False)
    del points["ten_sv"]
    for point in points:
        
        diem = points[point]
        if number.has_numbers(diem) == False:
            diem = "Chưa có điểm"
        embed.add_field(name=point, value=diem, inline=True)
    await message.channel.send(embed=embed)