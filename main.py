import discord, os

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.name == "suggestion":
        await message.add_reaction("✅")
        await message.add_reaction("❌")
    if message.channel.name == "faq":
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    if message.channel.name == "update-log":
        await message.add_reaction("👍")
        await message.add_reaction("👎")

client.run(os.environ["TOKEN"])