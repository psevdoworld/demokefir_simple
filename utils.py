import json
from aiohttp_stuff import get_requests
from db_stuff import insert_post_list

def populate_json(start=14241, end=14242, file='data.json'):
    data = {}
    data['links'] = ['https://habr.com/ru/post/' + str(i) + '/' for i in range(start,end)]

    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def get_links(file='data.json'):
    with open(file) as json_file:
        data = json.load(json_file)
    return data['links']

if __name__ == "__main__":
    populate_json(file='test_data.json')
    print(len(links := get_links(file='test_data.json')))
    requests = get_requests(links)
    posts_list = [list(post.get(i,"Nope") for i in ['url','status','title','text','time'])for post in  requests]
    insert_post_list(posts_list)

