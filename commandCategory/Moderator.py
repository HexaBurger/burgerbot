import twitchio
from .Category import Category

class ModeratorCategory(Category):
    name = "Moderator"

    def permission(chatter: twitchio.Chatter):
        return chatter.is_mod