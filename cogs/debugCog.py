import twitchio
from twitchio.ext import commands
from commandCategory.Debug import DebugCategory
import botFuncs
from minigames.gameManager import GameManager

class DebugCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.category = DebugCategory

    def hasPermission(self, chatter: twitchio.Chatter):
        return self.category.permission(chatter)

    @commands.command(name="hello", aliases=["hi", "heya"])
    async def helloCMD(self, ctx: commands.Context):
        if not self.hasPermission(ctx.author): return
        await ctx.send(f'Hello {ctx.author.display_name}!')

    @commands.command(name="echotest", aliases=[])
    async def echotestCMD(self, ctx: commands.Context, *, text: str):
        if not self.hasPermission(ctx.author): return
        await ctx.send(text)

    @commands.command(name="runningGames", aliases=[])
    async def getRunningGamesCMD(self, ctx: commands.Context):
        if not self.hasPermission(ctx.author): return
        gManager: GameManager = self.bot.gameManager
        await ctx.send(gManager.sessions)