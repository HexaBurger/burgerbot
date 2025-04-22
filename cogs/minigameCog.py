import twitchio
from twitchio.ext import commands
from commandCategory.Minigame import MinigameCategory
import botFuncs
from minigames.gameManager import GameManager

class MinigameCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.category = MinigameCategory

    def hasPermission(self, chatter: twitchio.Chatter):
        return self.category.permission(chatter)
    
    @commands.command(name="join", aliases=[])
    async def joinCMD(self, ctx: commands.Context):
        if not self.hasPermission(ctx.author): return
        gManager: GameManager = self.bot.gameManager
        out = await gManager.addPlayer(ctx.channel, ctx.message.author)
        if out: await ctx.channel.send(out)

    @commands.command(name="start", aliases=[])
    async def forceStartCMD(self, ctx: commands.Context):
        if not self.hasPermission(ctx.author): return
        gManager: GameManager = self.bot.gameManager
        out = await gManager.forceStart(ctx.channel, ctx.message.author)
        if out: await ctx.channel.send(out)

        