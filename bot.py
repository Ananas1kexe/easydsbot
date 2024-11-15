import discord
from discord.ext import commands
import os

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Мы залогинились как {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет!')

bot.run(TOKEN)
