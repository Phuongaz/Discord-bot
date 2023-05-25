import script_manager
from revChatGPT.V1 import Chatbot
from config import *

def __load__():
    script_manager.register_command("what", "ChatGPT command", "what")
    
def get_chatbot():
    return Chatbot(config= {
            "email": "vfkcxlgyvci@triots.com",
            "password": "$qAFi5^P"
        })

async def execute(data, message, *args):
    response = ""
    for data in get_chatbot().ask(
            message.content.replace(COMMAND_PREFIX + "what", "").strip()
    ):
        response = data["message"]
    if(response == "Hello! How can I assist you today?"):
        response = "Mày nói gì vậy, tao không hiểu?, có khi tao đang bị lỗi liên hệ Phương để fix"
    await message.channel.send(response)