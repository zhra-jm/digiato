from abc import ABC, abstractmethod
from config import LINK, CATEGORY
from models import Digiato, Link

import requests
from bs4 import BeautifulSoup

# from importer import LinkImporter
from parser import Parser


class CrawlerBase(ABC):

    @abstractmethod
    def start(self):
        pass

    @staticmethod
    def storing(data):
        pass

    @staticmethod
    def get_page(link):
        try:
            response = requests.get(link)
        except:
            return print(link)
        return response


class LinkCrawler(CrawlerBase):

    def __init__(self, category=CATEGORY, link=LINK):
        self.category = category
        self.link = link

    @staticmethod
    def find_links(html_doc, cat_name):
        tag_links = []
        soup = BeautifulSoup(html_doc, 'html.parser')
        for tag in soup.find_all('h3', attrs={'class': 'title'}):
            for a_tag in tag.find_all('a'):
                tag_links.append({'link': a_tag['href'], 'model_name': cat_name})
        return tag_links

    def start(self, store=False):
        links = []
        for cat in self.category:
            start = 0
            crawl = True
            while crawl:
                page = self.get_page(self.link.format(cat) + str(start))
                new_links = self.find_links(page.text, cat)
                links.extend(new_links)
                start += 1
                crawl = bool(len(new_links))
        links.extend(self.start_how())
        if store:
            self.storing(links)
        return links

    def start_how(self):
        links = []
        start = 0
        crawl = True
        while crawl:
            page = self.get_page('https://digiato.com/label/howstuffworks/page/' + f'{start}/')
            new_links = self.find_links(page.text, 'howstuffworks')
            start += 1
            links.extend(new_links)
            crawl = bool(len(new_links))

        return links

    @staticmethod
    def storing(links):
        Digiato.create_data_table()
        Link.link_importer(links)


class DataCrawler(CrawlerBase):

    def __init__(self):
        self.links = self.__load_links()
        self.parser = Parser()

    @staticmethod
    def __load_links():
        return Digiato.link_reader()

    def start(self, store=False):
        final_data = {'tech': [], 'mobile': [], 'car': [], 'business': [],
                      'howstuffworks': [], 'science': [], 'dgreview': []}
        for model, link in self.links.items():
            for li in link:
                response = self.get_page(li[0])
                data = self.parser.parse(response.text)
                final_data[model].append(data)
                Digiato.update_flag(li[1])
        if store:
            self.storing(final_data)

    @staticmethod
    def storing(data):
        Digiato.loader(data)
