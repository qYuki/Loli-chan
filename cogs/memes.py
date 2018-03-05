from discord.ext import commands


class Memes:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/memes/images/'

    @commands.command(pass_context=True)
    async def kappa(self, context):
        await self.bot.send_file(context.message.channel, '{}kappa.png'.format(self.base))

    @commands.command(pass_context=True, aliases=['tflip'])
    async def tableflip(self, context):
        await self.bot.send_file(context.message.channel, '{}tflip.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=['mrage'])
    async def megarage(self, context):
        await self.bot.send_file(context.message.channel, '{}mrage.png'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def yuno(self, context):
        await self.bot.send_file(context.message.channel, '{}yuno.png'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def troll(self, context):
        await self.bot.send_file(context.message.channel, '{}troll.png'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def booty(self, context):
        await self.bot.send_file(context.message.channel, '{}booty.gif'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def rekt(self, context):
        await self.bot.send_file(context.message.channel, '{}rekt.png'.format(self.base))

    @commands.command(pass_context=True, aliases=['cguy'])
    async def cerealguy(self, context):
        await self.bot.send_file(context.message.channel, '{}cereal.png'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def facepalm(self, context):
        await self.bot.send_file(context.message.channel, '{}picard.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def trolldance(self, context):
        await self.bot.send_file(context.message.channel, '{}trolldance.gif'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def ohyou(self, context):
        await self.bot.send_file(context.message.channel, '{}ohyou.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def foreveralone(self, context):
        await self.bot.send_file(context.message.channel, '{}foreveralone.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def pirate(self, context):
        await self.bot.send_file(context.message.channel, '{}pirate.png'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def notsure(self, context):
        await self.bot.send_file(context.message.channel, '{}notsure.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def sir(self, context):
        await self.bot.send_file(context.message.channel, '{}sir.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def cute(self, context):
        await self.bot.send_file(context.message.channel, '{}cute.png'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def hihi(self, context):
        await self.bot.send_file(context.message.channel, '{}hihi.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def hitler(self, context):
        await self.bot.send_file(context.message.channel, '{}hitler.jpg'.format(self.base))
	
    @commands.command(pass_context=True, aliases=[])
    async def goran(self, context):
        await self.bot.send_file(context.message.channel, '{}goran.jpg'.format(self.base))	
	
    @commands.command(pass_context=True, aliases=[])
    async def zoroja(self, context):
        await self.bot.send_file(context.message.channel, '{}zoroja.jpg'.format(self.base))	

    @commands.command(pass_context=True, aliases=[])
    async def sp(self, context):
        await self.bot.send_file(context.message.channel, '{}sp.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def natan(self, context):
        await self.bot.send_file(context.message.channel, '{}natan.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def zdenko(self, context):
        await self.bot.send_file(context.message.channel, '{}zdenko.jpg'.format(self.base))

    @commands.command(pass_context=True, aliases=[])
    async def jakob(self, context):
        await self.bot.send_file(context.message.channel, '{}jakob.jpg'.format(self.base))
		
    @commands.command(pass_context=True, aliases=[])
    async def hitler2(self, context):
        await self.bot.send_file(context.message.channel, '{}hitler2.jpg'.format(self.base))
		
def setup(bot):
    n = Memes(bot)
    bot.add_cog(n)
