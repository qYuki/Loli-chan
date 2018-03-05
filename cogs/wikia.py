from discord.ext import commands
import logging

from cogs.utils.chat_formatting import box
from __main__ import send_cmd_help

try:
    import wikia
except Exception as e:
    raise RuntimeError("You must run `pip3 install wikia` to use this cog") \
        from e

log = logging.getLogger("red.wikia")


class Wikia:
    def __init__(self, bot):
        self.bot = bot

    async def search(self, wiki, term):
        try:
            result = await self.bot.loop.run_in_executor(None, wikia.search,
                                                         wiki, term)
        except wikia.wikia.WikiaError:
            result = []
        return result

    async def summary(self, wiki, term):
        try:
            result = await self.bot.loop.run_in_executor(None, wikia.summary,
                                                         wiki, term)
        except wikia.wikia.WikiaError:
            result = ""
        return result

    async def page(self, wiki, title=None, page_id=None):
        return await self.bot.loop.run_in_executor(None, wikia.page,
                                                   title, page_id)

    @commands.group(pass_context=True)
    async def wikia(self, ctx):
        """Wikia related stuff"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @wikia.command(name="search", pass_context=True)
    async def _search(self, ctx, wiki, *, search_term):
        """Searches for a page"""
        channel = ctx.message.channel
        results = await self.search(wiki, search_term)
        msg = "Possiblities:\n"
        for result in sorted(results):
            msg += " - {}\n".format(result)
        await self.bot.send_message(channel, box(msg))

    @wikia.command(name="summary", pass_context=True)
    async def _summary(self, ctx, wiki, *, search_term):
        """Gets a summary from a wikia page"""
        channel = ctx.message.channel
        result = await self.summary(wiki, search_term)
        msg = "Summary from {}:\n{}".format(wiki, result)
        await self.bot.send_message(channel, box(msg))


def setup(bot):
    n = Wikia(bot)
    bot.add_cog(n)
