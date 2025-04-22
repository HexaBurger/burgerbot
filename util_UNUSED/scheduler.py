import asyncio
import time


class Scheduler:
    def __init__(self):
        self.scheduledEvents = dict()
        self.waiters = set()
        
