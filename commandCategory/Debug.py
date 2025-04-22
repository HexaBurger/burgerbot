import twitchio
from .Category import Category

class DebugCategory(Category):
    name = "Debug"

    def permission(chatter: twitchio.Chatter):
        return chatter.name in ["hexaburger","preiium"]