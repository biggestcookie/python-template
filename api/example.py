from aiohttp import ClientSession


API_BASE_URL = "https://api.nobelprize.org/2.1"


async def get_nobel_prizes():
    url = f"{API_BASE_URL}/nobelPrizes"
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
