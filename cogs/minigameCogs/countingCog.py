import twitchio
from twitchio.ext import commands
from commandCategory.Minigame import MinigameCategory
import botFuncs
from minigames.gameManager import GameManager
from minigames.counting import CountingMinigame

class Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.category = MinigameCategory

    def hasPermission(self, chatter: twitchio.Chatter):
        return self.category.permission(chatter)
    
    @commands.command(name="counting", aliases=[])
    async def countingMinigameCMD(self, ctx: commands.Context, playerCount: int | None):
        if not self.hasPermission(ctx.author): return
        if playerCount == None: playerCount = 4
        playerCount = max(1, min(8, playerCount))
        gManager: GameManager = self.bot.gameManager
        minigame = CountingMinigame(playerCount, ctx.message.author, ctx.channel)
        out = gManager.start(minigame)
        if out: await ctx.channel.send(out)
        else: await ctx.channel.send(f"A game of counting is starting soon! {ctx.prefix}join (30s)")

