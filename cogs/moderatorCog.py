import twitchio
from twitchio.ext import commands
from commandCategory.Moderator import ModeratorCategory
import botFuncs

class ModeratorCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.category = ModeratorCategory

    def hasPermission(self, chatter: twitchio.Chatter):
        return self.category.permission(chatter)