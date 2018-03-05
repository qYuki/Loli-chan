import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
# Sys
import aiohttp
import random
import os
import sys

DIR_DATA = "data/ohack"
SETTINGS = DIR_DATA+"/settings.json"

#API info:
#example: "/shit/10/20/rank/" - get 20 shit elements, start from 10th ordered by rank; noise: "/noise/{count=1; sql limit}/", 
#example: "/noise/50/" - get 50 random noise elements; model search: "/shit/model/{model; sql ilike}/", 
#example: "/shit/model/something/" - get all shit elements, where model name contains "something", ordered by id; author search: "/shit/author/{author; sql ilike}/", 
#example: "/shit/author/something/" - get all shit elements, where author name contains "something", ordered by id; get shit by id: "/shit/get/{id=0}/", 
#example: "/shit/get/6202/" - get shit element with id 6202; get shit count: "/shit/count/"; get noise count: "/noise/count/"; vote for shit: "/shit/vote/{id=0}/{operation=plus;[plus,minus]}/", 
#example: "/shit/vote/6202/minus/" - negative vote for shit with id 6202; vote for noise: "/noise/vote/{id=0}/{operation=plus;[plus,minus]}/", 
#example: "/noise/vote/57/minus/" - negative vote for noise with id 57;

#example: "/butts/10/20/rank/" - get 20 butts elements, start from 10th ordered by rank; noise: "/noise/{count=1; sql limit}/", 
#example: "/noise/50/" - get 50 random noise elements; model search: "/butts/model/{model; sql ilike}/", 
#example: "/butts/model/something/" - get all butts elements, where model name contains "something", ordered by id; author search: "/butts/author/{author; sql ilike}/", 
#example: "/butts/author/something/" - get all butts elements, where author name contains "something", ordered by id; get butts by id: "/butts/get/{id=0}/", 
#example: "/butts/get/6202/" - get butts element with id 6202; get butts count: "/butts/count/"; get noise count: "/noise/count/"; vote for butts: "/butts/vote/{id=0}/{operation=plus;[plus,minus]}/", 
#example: "/butts/vote/6202/minus/" - negative vote for butts with id 6202; vote for noise: "/noise/vote/{id=0}/{operation=plus;[plus,minus]}/", 
#example: "/noise/vote/57/minus/" - negative vote for noise with id 57;

clohack omegle:
    """The omegle/obutts.ru NSFW pictures of nature cog.
    https://github.com/Canule/Mash-Cogs
    """

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO(SETTINGS, "load")

    @commands.group(name="omegle", pohack_context=True)
    async def _omegle(self, ctx):
        """The omegle/obutts.ru pictures of nature cog."""        
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            return

    # shit
    @commands.command(pohack_context=True, no_pm=False)
    async def shit(self, ctx):
        """Shows some shit."""
        author = ctx.message.author
        nsfwChan = False
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                nsfwChan = True
                break
        try:
            rdm = random.randint(0, 10219)      
            search = ("http://l.omegle.com/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                boob = random.choice(result)
                boob = "http://l.omegle.com/".format(boob["preview"])
        except Exception as e:
            await self.bot.say("{} ` Error getting results.`".format(author.mention))
            return
        if not nsfwChan:
            await self.bot.say("{}".format(boob))
        else:
            await self.bot.send_message(ctx.message.author, "{}".format(boob))
            if self.settings["nsfw_msg"]:
                await self.bot.say("{}` nsfw content is not allowed in this channel, instead I have send you a DM.`".format(author.mention))

    # ohack
    @commands.command(pohack_context=True, no_pm=False)
    async def ohack(self, ctx):
        """Shows some ohack."""
        author = ctx.message.author
        nsfwChan = False
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                nsfwChan = True
                break
        try:
            rdm = random.randint(0, 4155)        
            search = ("http://l.omegle.com/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                ohack = random.choice(result)
                ohack = "http://l.omegle.com/{}".format(ohack["preview"])
        except Exception as e:
            await self.bot.say("{} ` Error getting results.`".format(author.mention))
            return
        if not nsfwChan:
            await self.bot.say("{}".format(ohack))
        else:
            await self.bot.send_message(ctx.message.author, "{}".format(ohack))
            if self.settings["nsfw_msg"]:
                await self.bot.say("{}` nsfw content is not allowed in this channel, instead I have send you a DM.`".format(author.mention))

    @checks.admin_or_permissions(manage_server=True)
    @_omegle.command(pohack_context=True, no_pm=False)
    async def nsfw(self, ctx):
        """Toggle omegle nswf for this channel on/off.
        Admin/owner restricted."""
        user= ctx.message.author
        nsfwChan = None
        # Reset nsfw.
        for a in self.settings["nsfw_channels"]:
            if a == ctx.message.channel.id:
                nsfwChan = True
                self.settings["nsfw_channels"].remove(a)
                await self.bot.say("{} ` nsfw ON`".format(user.mention))
                break
        # Set nsfw.
        if not nsfwChan:
            if ctx.message.channel not in self.settings["nsfw_channels"]:
                self.settings["nsfw_channels"].append(ctx.message.channel.id)
                await self.bot.say("{} ` nsfw OFF`".format(user.mention))
        fileIO(SETTINGS, "save", self.settings)
        
    @checks.admin_or_permissions(manage_server=True)
    @_omegle.command(pohack_context=True, no_pm=False)
    async def togglemsg(self, ctx):
        """Enable/Disable the omegle nswf not allowed message
        Admin/owner restricted."""
        user= ctx.message.author
        # Toggle
        if self.settings["nsfw_msg"]:
            self.settings["nsfw_msg"] = False
            await self.bot.say("{} ` DM nsfw channel msg is now: Disabled.`".format(user.mention))
        elif not self.settings["nsfw_msg"]:
            self.settings["nsfw_msg"] = True
            await self.bot.say("{} ` DM nsfw channel msg is now: Enabled.`".format(user.mention))
        fileIO(SETTINGS, "save", self.settings)

def check_folders():
    if not os.path.exists(DIR_DATA):
        print("Creating data/omegle folder...")
        os.makedirs(DIR_DATA)

def check_files():
    settings = {"nsfw_channels": ["133251234164375552"], "nsfw_msg": True}# Red's testing chan. nsfw content off by default.

    if not fileIO(SETTINGS, "check"):
        print("Creating settings.json")
        fileIO(SETTINGS, "save", settings)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(ohack(bot))


