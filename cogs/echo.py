import discord
from discord.ext import commands
import aiohttp
import random

class Echo:
    """Says what you want"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, *, text):
        """Type and the bot will say it."""
        await self.bot.say("{}".format(text))

def setup(bot):
    bot.add_cog(Echo(bot))
