import json

def populate_json(start=14241, end=14242, file='data.json'):
    data = {}
    data['links'] = ['https://habr.com/ru/post/' + str(i) + '/' for i in range(start,end)]

    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def get_links(file='data.json'):
    with open(file) as json_file:
        data = json.load(json_file)
    return data['links']

