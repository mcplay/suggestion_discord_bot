import discord, os

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.name == "suggestion":
        await message.add_reaction("👍")
        await message.add_reaction("👎")

client.run(os.environ["TOKEN"])