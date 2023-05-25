import asyncio
from config import *
from modules import watch_point
from modules import anime_news
async def load_modules(bot):
    ## portal vhu
    portal_vhu = bot.get_channel(CHANNEL_VHU_SCORE)
    #await portal_vhu.send("Listen vhu portal!")
    loop = asyncio.get_event_loop()
    loop.create_task(watch_point.listen(portal_vhu))
    ## anime news
    anime_channel = bot.get_channel(CHANNEL_ANIME_NEWS)
    #await anime_channel.send("Listen anime47.com!")
    loop = asyncio.get_event_loop()
    loop.create_task(anime_news.listen(anime_channel))
    