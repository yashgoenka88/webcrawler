from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin

class Crawler():

    def  __init__(self, url,level):
        self.url = url
        self.level = level
        self.tld = urlparse(url).hostname

    def link_structure(self):
        return {
            "url":"",
            "links":[],
            "level":1
        }

    def filter_domain(self, link):
        return self.tld == link.hostname or link.hostname == 'www.' + self.tld or link.hostname == None

    def is_valid(self, url):
        return url is not '#' and url is not None and (urlparse(url).scheme == 'http' or urlparse(url).scheme == 'https')

    def crawl(self, url, level):
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        links = []

        for link in soup.find_all('a'):

            href = link.get('href')

            link_structure = self.link_structure()
            link_structure['level'] = level + 1
            link_structure['url'] = href if urlparse(href).hostname is not None else urljoin(self.url, href)

            if not any(link_structure['url'] == d['url'] for d in links) and link_structure['url'] is not url and self.is_valid(link_structure['url']) and self.filter_domain(urlparse(link_structure['url'])):

                if link_structure['level'] <= int(self.level) and link_structure['url'] is not self.url:
                    link_structure['links'] = self.crawl(link_structure['url'], link_structure['level'])


                links.append(link_structure)

        return links


    def fetch(self):
        try:
            root = self.link_structure()

            root['url'] = self.url

            root['links'] = self.crawl(root['url'], root['level'])

            return root
        except:
            raise Exception