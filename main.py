import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.environ['DISCORD_APP_TOKEN'])
