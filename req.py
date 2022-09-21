from aiohttp import ClientSession
import asyncio


async def get_response():
    async with ClientSession(
            base_url='https://catalog.onliner.by'
    ) as session:
        async with session.get(
                url='/sdapi/catalog.api/search/player',
                params={
                    'player_type[0]': 'hifiplayer',
                    'player_type[operation]': 'union',
                    'group': 1
                }
        ) as response:
            print(response.status)
            print(response.headers)
            print(await response.text())
            print(await response.json())


asyncio.run(get_response())

# from requests import Session
#
#
# def get_response():
#     with Session() as session:
#         session.headers.update({'Accept-Language': 'ru'})
#         response = session.get(
#             url='https://catalog.onliner.by/sdapi/catalog.api/search/player',
#             params={
#                 'player_type[0]': 'hifiplayer',
#                 'player_type[operation]': 'union',
#                 'group': 1
#
#             }
#         )
#         print(response.status_code)
#         print(response.text)
#         print(response.json())
# get_response()
