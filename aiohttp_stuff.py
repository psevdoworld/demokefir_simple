import random
import asyncio
from aiohttp import ClientSession
from parsing import parse_document

async def fetch(url, session):
    async with session.get(url) as response:
        
        return parse_document(await response.text(), url)


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        return await fetch(url, session)


async def run(links):
    url = "http://localhost:8080/{}"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for url in links:
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        return await responses

def get_requests(links):
    loop = asyncio.get_event_loop()

    future = asyncio.ensure_future(run(links))
    loop.run_until_complete(future)
    return future.result()
