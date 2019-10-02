from discord.ext import commands
from annotation.futebot import command


@command
@commands.command()
async def listall(ctx):
    await ctx.send("```--- Commands List --- \n"
                   ".coach                                      - Returns a random motivational quote\n"
                   ".gifme     {search_term}                    - Search for a Gif\n"
                   ".horoscopo {horoscopo}                      - Search for you daily horoscope\n"
                   ".ping      {optional_name}                  - Check if bot is Alive with optional mention\n"
                   ".youtube   {search_term}                    - Search for a Youtube Video\n"
                   ".imgme     \"{search_term}\" {--spoiler}    - Search for an image in Google\n"
                   ".gifme     \"{search_term}\" {--spoiler}    - Search for an gif in Google\n"
                   ".soniko    {caption}                        - Create a Soniko meme\n"
                   ".speech    {caption}                        - Speech Meme\n"
                   "```")
