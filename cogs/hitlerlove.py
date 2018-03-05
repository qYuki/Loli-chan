import discord
from discord.ext import commands
import random

class Hitlerlove:
    """Penis related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hitlerlove(self, user : discord.Member):
        """Detects user's penis length

        This is 100% accurate."""
        random.seed(user.id)
        p = "Hiter love meter: " + "<:hitler:255003431746404362>"*random.randint(0, 10) + "."
        await self.bot.say(p)

def setup(bot):
    bot.add_cog(Hitlerlove(bot))
