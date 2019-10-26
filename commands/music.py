from discord.ext import commands
from util.helpers import spotify_auth

from annotation.futebot import command


@command(desc="Pesquisa e retorna uma musica do spotify, usar '""' para pesquisas com mais de uma palavra ")
async def musica(ctx, musica):
    try:
        sp = spotify_auth()
        results = sp.search(musica, limit=1)
        for track in results["tracks"]["items"]:
            response = track["external_urls"]["spotify"]

        await ctx.send(response)

    except Exception as e:
        await ctx.send(e)
