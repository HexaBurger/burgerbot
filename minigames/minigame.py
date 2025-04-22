import twitchio
import time
class Minigame:
    def __init__(self, maxPlayers: int, player: twitchio.Chatter, channel: twitchio.Channel):
        self.maxPlayers = maxPlayers
        self.players = [player] # index 0 - host
        self.channel = channel
        self.status = 0 # 0 - awaiting for players, 1 - active, 2 - has ended
        self.startTime = time.time()
        self.lastTime = time.time()
        self.awaitTimeout = 30
        self.gameTimeout = 10

    async def start(self):
        self.status = 1
        self.lastTime = time.time()
        self.startTime = time.time()
        await self.channel.send("Minigame has started")
    
    async def end(self):
        self.status = 2
        await self.channel.send("Minigame has ended")

    async def handleMessage(self, message: twitchio.Message):
        pass

    @property
    def totalTime(self):
        return time.time() - self.startTime
    
    @property
    def timer(self):
        return time.time() - self.lastTime