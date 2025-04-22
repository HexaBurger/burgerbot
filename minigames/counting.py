import twitchio
import time
import random
from .minigame import Minigame

class CountingMinigame(Minigame):
    def __init__(self, maxPlayers: int, player: twitchio.Chatter, channel: twitchio.Channel):
        self.maxPlayers = maxPlayers
        self.players = [player] # index 0 - host
        self.channel = channel
        self.status = 0 # 0 - awaiting for players, 1 - active, 2 - has ended
        self.startTime = time.time()
        self.lastTime = time.time()
        self.awaitTimeout = 30
        self.gameTimeout = 30
        self.scores = []
        self.nextNumber = 1

    async def start(self):
        self.scores = [0 for p in self.players]
        await self.channel.send("Counting has started! Add values to the count to progress.")
        await self.channel.send("Start counting from 1")
        self.status = 1
        self.lastTime = time.time()
        self.startTime = time.time()
    
    async def end(self):
        self.status = 2
        totalScore = sum(self.scores)
        playerScores = f"{self.players[0].display_name} - {self.scores[0]}"
        for i in range(1, len(self.players)):
            playerScores += f", {self.players[i].display_name} - {self.scores[i]}"
        await self.channel.send(f"Game over! The correct number was {self.nextNumber}.")
        await self.channel.send(f"Total score: {totalScore}. Individual scores: {playerScores}.")
        await self.channel.send(f"Counting has ended. ({int(self.totalTime)}s)")

    async def handleMessage(self, message: twitchio.Message):
        text: str = message.content
        if not text.isdigit(): return 0
        player = message.author
        num = int(text)
        totalScore = sum(self.scores)
        if num == self.nextNumber:
            playerIndex = self.players.index(player)
            self.scores[playerIndex] += 1
            self.gameTimeout = max(10, 30 - 2 * totalScore)
            numMax = (totalScore // 5 + 2) * 10
            value = random.randint(totalScore, numMax)
            self.nextNumber += value
            await self.channel.send(f"+{value}")
            self.lastTime = time.time()
        else:
            await self.end()
        
        return 1
