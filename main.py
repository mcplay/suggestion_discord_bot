import discord, os

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.name == "test":
        await message.add_reaction("✅")
        await message.add_reaction("❌")

client.run(os.environ["TOKEN"])