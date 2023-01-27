import asyncio
import websockets
import json
import certifi
ca = certifi.where()

async def hello():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@bookTicker") as ws:
        while True:
            response = await asyncio.wait_for(ws.recv(), timeout=2)
            response=json.loads(response)
            print(response)
            await asyncio.sleep(0.5)

asyncio.get_event_loop().run_until_complete(hello())