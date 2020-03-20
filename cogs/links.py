import discord
import config
from discord.ext import commands
from discord.ext.commands import Cog

class Links(Cog):
    """
    Commands for easily linking to projects.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, aliases=["xyproblem"])
    async def xy(self, ctx):
        """Link to the "What is the XY problem?" post from SE"""
        await ctx.send("<https://meta.stackexchange.com/q/66377/285481>\n\n"
                       "TL;DR: It's asking about your attempted solution "
                       "rather than your actual problem.\n"
                       "It's perfectly okay to want to learn about a "
                       "solution, but please be clear about your intentions "
                       "if you're not actually trying to solve a problem.")

    @commands.command(hidden=True, aliases=["guides", "link"])
    async def guide(self, ctx):
        """Link to the guide(s)"""

        message_text=("**Generic starter guides:**\n"
                      "AtlasNX's Guide: "
                      "<https://guide.teamatlasnx.com>\n"
                      "\n"
                      "**Specific guides:**\n"
                      "Manually Updating/Downgrading (with HOS): "
                      "<https://guide.sdsetup.com/usingcfw/manualupgrade>\n"
                      "Manually Repairing/Downgrading (without HOS): "
                      "<https://guide.sdsetup.com/usingcfw/manualchoiupgrade>\n"
                      "Setting up EmuMMC (Windows): "
                      "<https://switch.homebrew.guide/emummc/windows>\n"
                      "Setting up EmuMMC (Linux): "
                      "<https://switch.homebrew.guide/emummc/linux>\n"
                      "Setting up EmuMMC (Mac): "
                      "<https://switch.homebrew.guide/emummc/mac>\n"
                      "How to get started developing Homebrew: "
                      "<https://switch.homebrew.guide/homebrew_dev/introduction>\n"
                      "\n")

        try:
            support_faq_channel = self.bot.get_channel(config.support_faq_channel)
            if support_faq_channel is None:
                message_text += "Check out #support-faq for additional help."
            else:
                message_text += f"Check out {support_faq_channel.mention} for additional help."
        except AttributeError:
            message_text += "Check out #support-faq for additional help."
        
        await ctx.send(message_text)

    @commands.command(hidden=True, aliases=["patron"])
    async def patreon(self, ctx):
        """Link to the patreon"""
        await ctx.send("https://www.patreon.com/werwolv")    

    @commands.command()
    async def source(self, ctx):
        """Gives link to source code."""
        await ctx.send(f"You can find my source at {config.source_url}. "
                       "Serious PRs and issues welcome!")

    @commands.command(aliases=['edz'])
    async def edizon(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xf5a623))

        embed.set_author(name="Links", url="http://werwolv.net", icon_url="https://raw.githubusercontent.com/WerWolv/EdiZon/master/icon.jpg")

        embed.add_field(name="__EdiZon Release__", value="**NRO:** https://github.com/WerWolv/EdiZon/releases/latest\n**Cheats/Configs:** http://werwolv.net/api/edizon/v2/build.zip")
        embed.add_field(name="__EdiZon Nightly__", value="**NRO:** https://github.com/WerWolv/EdiZon/releases/tag/snapshot\n**Cheats/Configs:** http://werwolv.net/api/edizon/v3/build.zip")
        embed.add_field(name="__GitHub repos__", value="**EdiZon:** https://github.com/WerWolv/EdiZon\n**Database:** https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts")

        await ctx.send(embed=embed)

    @commands.command(aliases=['tsl'])
    async def tesla(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0x017fca))

        embed.set_author(name="Tesla Links", url="https://gbatemp.net/threads/tesla-the-nintendo-switch-overlay-menu.557362/", icon_url="https://media.discordapp.net/attachments/553529173420015619/673618681263292426/tesla_experimentLogo.png")

        embed.add_field(name="__nx-ovlloader__", value="**Download:** https://github.com/WerWolv/nx-ovlloader/releases/latest")
        embed.add_field(name="__Tesla Menu__", value="**Download:** https://github.com/WerWolv/Tesla-Menu/releases/latest")
        embed.add_field(name="__libtesla__", value="**Download:** https://github.com/WerWolv/libtesla/releases/latest")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Links(bot))
