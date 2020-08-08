from utils import get_links
from aiohttp_stuff import get_requests
from db_stuff import insert_post_list

links = get_links()
posts_list = [list(post.get(i,"Nope") for i in ['url','status','title','text','time'])for post in  get_requests(links)]
insert_post_list(posts_list)
