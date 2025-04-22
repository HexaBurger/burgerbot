import twitchio
import asyncio
from minigames.minigame import Minigame

class GameManager:
    def __init__(self):
        self.sessions: dict[twitchio.Channel,Minigame] = dict()

    def start(self, minigame:Minigame):
        if minigame.channel in self.sessions.keys():
            return "Another game is active at the moment! glorp"
        self.sessions[minigame.channel] = minigame
        return 0
    
    async def addPlayer(self, channel: twitchio.Channel, player: twitchio.Chatter):
        if not channel in self.sessions: return "There currently isn't an active game."
        session = self.sessions[channel]
        if player in session.players: return "You already joined this game."
        if session.status != 0: return 0

        session.players.append(player)
        playerCount = session.players.__len__()
        maxPlayers = session.maxPlayers
        await channel.send(f"{player.display_name} has joined! {playerCount}/{maxPlayers} ({int(session.awaitTimeout - session.timer)}s)")

        if playerCount >= maxPlayers:
            await self.sessions[channel].start()
        return 0

    async def forceStart(self, channel: twitchio.Channel, player: twitchio.Chatter):
        if not channel in self.sessions: return "There currently isn't an active game."
        if self.sessions[channel].status != 0: return 0
        if not player in self.sessions[channel].players: return "You are not the host of this game."
        if self.sessions[channel].players[0] != player: return "You are not the host of this game."

        await self.sessions[channel].start()
        return 0

    async def handleMessage(self, message: twitchio.Message):
        channel = message.channel
        author = message.author
        if not channel in self.sessions: return 0
        if not author in self.sessions[channel].players: return 0
        if self.sessions[channel].status == 0: return 0

        return await self.sessions[channel].handleMessage(message)

    async def update(self):
        while True:
            for session in self.sessions.values():
                match session.status:
                    case 0:
                        if session.timer > session.awaitTimeout: await session.start()
                    case 1:
                        if session.timer > session.gameTimeout: await session.end()
                    case 2:
                        self.sessions.pop(session.channel)        
            await asyncio.sleep(1)
            