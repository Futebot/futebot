from discord.ext import commands


@commands.command()
async def listall(ctx):
    await ctx.send("```--- Commands List --- \n"
                   ".coach                                       - Returns a random motivational quote\n"
                   ".dictionary {term}                           - Returns a defintion of a single word in pt-br\n"
                   ".gifme      {search_term}                    - Search for a Gif\n"
                   ".horoscopo  {horoscopo}                      - Search for you daily horoscope\""
                   ".ping       {optional_name}                  - Check if bot is Alive with optional mention\""
                   ".youtube    {search_term}                    - Search for a Youtube Video\n"
                   ".imgme      \"{search_term}\" {--spoiler}    - Search for an image in Google\n"
                   ".gifme      \"{search_term}\" {--spoiler}    - Search for an gif in Google\n"
                   ".soniko     {caption}                        - Create a Soniko meme\n"
                   ".speech     {caption}                        - Speech Meme\n"
                   "```")
