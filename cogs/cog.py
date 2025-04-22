import twitchio
from twitchio.ext import commands
from commandCategory.Category import Category
import botFuncs

class Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.category = Category

    def hasPermission(self, chatter: twitchio.Chatter):
        return self.category.permission(chatter)
    
    @commands.command(name="Name", aliases=[])
    async def command(self, ctx: commands.Context):
        if not self.hasPermission(ctx.author): return