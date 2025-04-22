import twitchio
import importlib
import os
import inspect
import asyncio

from cogs.cog import Cog as BotCog
from dotenv import load_dotenv
from twitchio.ext import commands
from botFuncs import *
from minigames.gameManager import GameManager

load_dotenv()

abspath = os.path.abspath(__file__)
os.chdir(os.path.dirname(abspath))

botUsername = "daborgorbot"

class Bot(commands.Bot):

    def __init__(self,token,prefix,initial_channels):
        super().__init__(token=token, prefix=prefix, initial_channels=initial_channels)
        self.gameManager = GameManager()
        self.loadCogs()
        asyncio.Task(self.gameManager.update())

    def loadCogs(self):
        modules = self.loadModules(os.path.join(os.getcwd(), "cogs"), "cogs")
        for module in modules:
            imported = importlib.import_module(module)
            for _, cog in imported.__dict__.items():
                if inspect.isclass(cog) and issubclass(cog, commands.Cog) and cog != BotCog: self.add_cog(cog(self))

    def loadModules(self, path, module):
        modules = []
        for file in os.listdir(path):
            if file == "__pycache__": continue
            if os.path.isdir(os.path.join(path, file)):
                for submodule in self.loadModules(os.path.join(path,file),f"{module}.{file}"):
                    modules.append(submodule)
            elif os.path.isfile(os.path.join(path, file)) and file.endswith(".py"):
                modules.append(f"{module}.{file[:-3]}")
        return modules

    async def event_ready(self):
        print(f'{self.nick} has logged on')
        print(f'User id: {self.user_id}')

    async def event_message(self, message: twitchio.Message):
        if type(message.author) != type(None):
            if await self.gameManager.handleMessage(message): return
            await self.handle_commands(message)



channelList = ['hexaburger']


bot = Bot(os.getenv("TOKEN"),"?",channelList)
bot.run()