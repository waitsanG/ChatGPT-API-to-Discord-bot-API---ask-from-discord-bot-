import os
import discord
from discord.ext import commands
import openai
from asyncio_throttle import Throttler



# Set OpenAI API key
openai.api_key = "key1"

# Create a new bot with all intents enabled
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Create a new bot with all intents enabled
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ask(ctx, *, prompt):
    # Call OpenAI API to complete prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get completed text and send to Discord channel
    completed_text = response["choices"][0]["text"]
    await ctx.message.channel.send(completed_text)

bot.run("Key2")
