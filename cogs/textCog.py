import twitchio
from twitchio.ext import commands
from commandCategory.Text import TextCategory
import botFuncs

class TextCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.category = TextCategory

    def hasPermission(self, chatter: twitchio.Chatter):
        return self.category.permission(chatter)

    @commands.command(name="corpusspeech", aliases=["corpus", "corpusify"])
    async def corpusSpeechCMD(self, ctx: commands.Context, *, text: str):
        if not self.hasPermission(ctx.author): return
        await ctx.send(botFuncs.corpusSpeech(text[1]))

    @commands.command(name="score", aliases=[])
    async def nameScoreCMD(self, ctx: commands.Context, keyword: str, target: twitchio.PartialChatter):
        if not self.hasPermission(ctx.author): return
        await ctx.send(f"{target.name}'s {keyword} score is {botFuncs.nameScore(keyword, target.name):.2f}.")
