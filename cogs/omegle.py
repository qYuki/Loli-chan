import discord
from discord.ext import commands
import aiohttp
import random

class Omegle:
    """Time to grab Omegle conversations."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def omegle(self, *, search_terms : str):
        """Grabs an Omegle conversation"""
        await self.bot.say("http://l.omegle.com/{}.png".format(search_terms))

def setup(bot):
    bot.add_cog(Omegle(bot))
