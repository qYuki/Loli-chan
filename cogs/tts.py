import discord
from discord.ext import commands
import aiohttp
import random

class Texttospeech:
    """Text to speech"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, *, search_terms : str):
        """Text to speech"""
        await self.bot.say("{}".format(search_terms), tts=True)

def setup(bot):
    bot.add_cog(Texttospeech(bot))
