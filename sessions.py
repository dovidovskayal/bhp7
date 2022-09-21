from aiohttp import ClientSession
import asyncio

async def get_wss():
    async with ClientSession() as session:
        async with session.ws_connect(
            url='wss://demo.piesocket.com/v3/channel_1?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self'
        ) as wss:
            async for message in wss:
                print(message.data)
                #await wss.send_str('in')

asyncio.run(get_wss())