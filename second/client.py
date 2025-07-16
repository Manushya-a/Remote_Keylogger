import asyncio
import websockets
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ORANGE = '\033[38;5;208m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    MAGENTA = '\033[95m'
    UNDERLINE = '\033[4m'

async def client():
    uri = "ws://Your.I.P.Address:8765"

    async with websockets.connect(uri) as websocket:
        print(bcolors.OKGREEN + f"Connected to {uri}" + bcolors.ENDC)
        message = input("Whats your message: ")

        await websocket.send(message)
        print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.ENDC + f"Message sent: {message}")

        response = await websocket.recv()
        print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.ENDC + f"Received Message {response}")

if __name__ == "__main__":
    asyncio.run(client())