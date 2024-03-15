import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv() 

bot = commands.Bot(command_prefix='!')

# Load the welcome cog
bot.load_extension("cogs.welcome")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))
