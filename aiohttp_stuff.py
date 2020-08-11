import random
import asyncio
from aiohttp import ClientSession
from parsing import parse_document
from db_stuff import insert_post
async def fetch(url, session):
    async with session.get(url) as response:

        post = parse_document(await response.text(), url)
        post_list = list(post.get(i,"Nope") for i in ['url','status','title','text','time'])
        insert_post(post_list)


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(url, session)


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
        await responses

def get_and_save_requests(links):
    loop = asyncio.get_event_loop()

    future = asyncio.ensure_future(run(links))
    loop.run_until_complete(future)
