from bs4 import BeautifulSoup

def parse_document(r_text, url):
    soup = BeautifulSoup(r_text, 'html5lib')
    doc = {'url':url}

    if not soup.find('span', {'class': 'post__title-text'}):
        doc['status'] = 'title_not_found'
    else:
        doc['status'] = 'ok'
        doc['title'] = soup.find('span', {'class': 'post__title-text'}).text
        doc['text'] = soup.find('div', {'class': 'post__text'}).text
        doc['time'] = soup.find('span', {'class': 'post__time'}).text


    return doc
