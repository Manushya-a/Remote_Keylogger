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

async def client_handler(websocket):
    try:
        while True:
            message = input(f"{bcolors.OKCYAN}What is your message (or 'quit' to exit): {bcolors.ENDC}")
            
            if message.lower() == 'quit':
                await websocket.send(message)
                print(f"{bcolors.YELLOW}Closing connection...{bcolors.ENDC}")
                await websocket.close()
                break
                
            if message == "?":
                print(f"{bcolors.OKGREEN}Connection status: {websocket}{bcolors.ENDC}")
                continue
                
            await websocket.send(message)
            print(f"{bcolors.OKBLUE}[Sent] {message}{bcolors.ENDC}")
            
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                print(f"{bcolors.MAGENTA}[Received] {response}{bcolors.ENDC}")
            except asyncio.TimeoutError:
                print(f"{bcolors.ORANGE}No response received (timeout){bcolors.ENDC}")
                
    except websockets.exceptions.ConnectionClosed:
        print(f"{bcolors.RED}Connection closed by server{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.RED}Error: {str(e)}{bcolors.ENDC}")

async def main():
    uri = "ws://Your.I.P.Adrress:8765"
    
    try:
        async with websockets.connect(uri, ping_interval=20, ping_timeout=60) as websocket:
            print(f"{bcolors.OKGREEN}Connected to {uri}{bcolors.ENDC}")
            print(f"{bcolors.HEADER}Type '?' to check connection, 'quit' to exit{bcolors.ENDC}")
            await client_handler(websocket)
            
    except websockets.exceptions.WebSocketException as e:
        print(f"{bcolors.RED}Connection error: {str(e)}{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.RED}Unexpected error: {str(e)}{bcolors.ENDC}")
    finally:
        print(f"{bcolors.YELLOW}Client terminated{bcolors.ENDC}")

if __name__ == "__main__":
    asyncio.run(main())