import asyncio
import string
from tkinter import Tk, filedialog
from .memory import MemoryInterface # type: ignore
import aioconsole


class FTLArchipelagoClient:
    def __init__(self):
        self.running = True
        self.state = {}

    async def run(self):
        await self.start()
        while self.running:
            await self.update()
    
    async def start(self):
        print("Initializing client...")

        self.exe_path = await self.select_exe()

        self.mem = MemoryInterface(self.exe_path) # setup memory

        await self.connect_to_archipelago()

    async def update(self):


        recieved_mesage = self.check_incoming()

        self.send_outgoing(recieved_mesage)

        await asyncio.sleep(0.1) # 10 Hz

    def select_exe_sync(self):
        root = Tk()
        root.withdraw()
        return filedialog.askopenfilename(
            title="Select FTLGame.exe",
            filetypes=[("Executable Files", "FTLGame.exe")],
        )

    async def select_exe(self):
        return await asyncio.to_thread(self.select_exe_sync)

    async def connect_to_archipelago(self):
        # Set up websocket connection etc.
        pass

    def check_incoming(self) -> string:
        message = self.mem.check_message()

        if message == None:
            return

        # send messages through to archipelago
        return message

    def send_outgoing(self, recieved_message):
        if recieved_message == "Started new run":
            self.mem.send_message("recieved SCRAPx1000")

    def exit(self):
        self.running = False
        # cleanly close memory manager, websocket, etc.
        pass
