import script_manager
from modules.operator import operator

def __load__():
    script_manager.register_command("op", "Operator command", "operator")

async def execute(data, message, *args):
    print(message.author.id)
    op = operator.Operator()
    if op.is_operator(message.author.id):
        if args[0] is not None:
            if args[0] == "add":
                if len(args) == 2:
                    op.add_operator(args[1])
                    await message.channel.send("Added " + args[1] + " to operator list")
                else:
                    await message.channel.send("Invalid arguments")
            elif args[0] == "remove":
                if len(args) == 2:
                    op.remove_operator(args[1])
                    await message.channel.send("Removed " + args[1] + " from operator list")
                else:
                    await message.channel.send("Invalid arguments")
            elif args[0] == "list":
                await message.channel.send("Operator list: " + str(op.get_operator_list()))
            else:
                await message.channel.send("Invalid arguments")
        else:
            await message.channel.send("Invalid arguments")
    else:
        await message.channel.send("You are not operator")