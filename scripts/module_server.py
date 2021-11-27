import script_manager
import requests
import discord

def __load__():
    script_manager.register_command("server", "Check server", "server")

async def execute(data, message, *args):
    servers = {"lobby": "play.locmvn.net:19132", "survival" : "", "skyblock": "", "prison": ""}
    if args[0][1] in servers:
        response = requests.get("https://api.mcsrvstat.us/bedrock/2/" + servers[args[0][1]])
        embed = discord.Embed(title="SERVER " + args[0][1].upper())
        if response.json()["online"]:
            players = response.json()['players']
            embed.add_field(name=args[0][1], value=str(players["online"]) + "/" + str(players["max"]))
        else:
            embed.add_field(name=args[0][1], value="Server offline")
        await message.channel.send(embed=embed)
        return
    await message.channel.send("Server "+ args[0][1] +" not found")