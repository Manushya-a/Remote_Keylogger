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


async def server(websocket):
    message = await websocket.recv()
    print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.ENDC + f"Server Recieved: {message}!")

    gretting = input("Your response: ")
    await websocket.send(gretting)

async def main():
    async with websockets.serve(server, "0.0.0.0", 8765):
        print("Websocket sever starte and listenig on YOUR.IP.ADDRE.SS:8765")
        await asyncio.Future() # Run forever


if __name__ == "__main__":
    asyncio.run(main())