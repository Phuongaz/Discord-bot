import curio
import sys
import os

async def start():
    
    print("Listening console")
    
    while True:
        user_input = await curio.run_in_thread(input)
        input_list = user_input.strip().split(" ")
        if input_list[0] == "exit":
            sys.exit()
        elif input_list[0] == "reload":
            print("Reloading...")
            python = sys.executable
            os.execl(python, python, * sys.argv)