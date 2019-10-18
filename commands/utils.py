from discord.ext import commands

from .config import BOT_DEV_PREFIX, BOT_ENV, BOT_ENV_PROD, BOT_PROD_PREFIX

prefix = BOT_PROD_PREFIX if BOT_ENV == BOT_ENV_PROD else BOT_DEV_PREFIX

bot = commands.Bot(command_prefix=prefix)
