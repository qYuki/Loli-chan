from discord.ext import commands


class Images:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/images/'

    @commands.command(pass_context=True)
    async def hitler(self, context):
        await self.bot.send_file(context.message.channel, '{}hitler.png'.format(self.base))

    @commands.command(pass_context=True, aliases=['goran'])
    async def goran(self, context):
        await self.bot.send_file(context.message.channel, '{}goran.jpg'.format(self.base))

    


def setup(bot):
    n = Images(bot)
    bot.add_cog(n)
