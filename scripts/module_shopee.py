import script_manager
from config import *
from modules import shopee_ship
import asyncio

def __load__():
    script_manager.register_command("runshopee", "Loop check shopee", "shopee")

async def execute(data, message, *args):
    loop = asyncio.get_event_loop()
    loop.create_task(shopee_ship.run_shopee_thread(message))