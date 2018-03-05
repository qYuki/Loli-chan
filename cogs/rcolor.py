import discord
from discord.ext import commands
import random

class Randomcolor:
    """Random color command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rcolor(self, user : discord.Member):
        """Random color"""
		
		await self.bot.say("*The color is... " + choice(["Red", "Green", "Black"]))

def setup(bot):
    bot.add_cog(Randomcolor(bot))
