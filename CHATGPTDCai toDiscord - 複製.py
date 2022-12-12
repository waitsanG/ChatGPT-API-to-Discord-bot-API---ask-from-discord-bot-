import os
import openai
import discord
import requests
from discord.ext import commands
from io import BytesIO
from keep_alive import keep_alive


# Get API keys from environment variables
#delete if you useing another Token storeage
key1 = os.environ['openaikey']
key2 = os.environ['discordkey']


#enter your OPENAI API TOKEN replace key1
openai.api_key = key1

#Create a new bot with all intents enabled
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ask(ctx, *, prompt):
    # Call OpenAI API to complete prompt useing command !ask <question>
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,)

    # Get completed text and send to Discord channel
    completed_text = response["choices"][0]["text"]
    await ctx.message.channel.send(completed_text)

@bot.command()
async def img(ctx, *, prompt):
    # Call OpenAI API to generate image useing !img <image tag>
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=1,
        size="1024x1024",)

    # Get generated image URL and download image
    image_url = response["data"][0]["url"]
    img_data = requests.get(image_url).content

    # Send generated image to Discord channel
    await ctx.message.channel.send(file=discord.File(BytesIO(img_data), "generated_image.jpg"))
	
keep_alive()
#enter your discord API TOKEN replace key2
bot.run(key2)
