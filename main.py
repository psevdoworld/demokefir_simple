from utils import get_links
from aiohttp_stuff import get_requests
from db_stuff import insert_post_list

links = get_links() #получаем ссылки из json
requests = get_requests(links) # в результате асинхронной магии с щепоткой bs4 получаем данные страниц
posts_list = [list(post.get(i,"Nope") for i in ['url','status','title','text','time'])for post in  requests] # небольшая конвертация в неловкий список для бд
# был плавающий баг, но я не уверен что он ушел. Иногда данные одних и тех же страниц не получаются
insert_post_list(posts_list) # бд завершает начатое
