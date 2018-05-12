import smmrpy
import aiohttp
import asyncio
import analyzer

async def fetch(url):
    s = smmrpy.SMMRPY('8B1BD1A777') # Instantiate the SMMRPY instance.
    article = await s.get_smmry(url)
    a = article.content
    return a

def summarize(url):
    res = ""
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(fetch(url))
    loop.close()
    return res

