import discord, os

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.name == "suggestion":
        await message.add_reaction(":white_check_mark:")
        await message.add_reaction(":x:")
    if message.channel.name == "faq":
        await message.add_reaction(":thumbsup:")
        await message.add_reaction(":thumbsdown:")
    if message.channel.name == "update-log":
        await message.add_reaction(":thumbsup:")
        await message.add_reaction(":thumbsdown:")

client.run(os.environ["TOKEN"])