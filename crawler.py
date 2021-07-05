from abc import ABC, abstractmethod
from config import LINK, CATEGORY
from models import Technology, Mobile, Car, Business,HowStuffWorks, Science, Review

import requests
from bs4 import BeautifulSoup

from importer import BaseImporter
from models import Digiato
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
        except requests.HTTPError:
            return None
        print(response.status_code)


class LinkCrawler(CrawlerBase):

    def __init__(self, category=CATEGORY, link=LINK):
        self.category = category
        self.link = link

    @staticmethod
    def find_links(html_doc):
        tag_links = []
        soup = BeautifulSoup(html_doc, 'html.parser')
        for tag in soup.find_all('h3', attrs={'class': 'title'}):
            for a_tag in tag.find_all('a'):
                tag_links.append({'link': a_tag['href']})
        return tag_links

    def crawl_page(self, link):
        start = 0
        links = []
        crawl = True
        while crawl:
            page = self.get_page(link + str(start))
            new_links = self.find_links(page.text)
            links.extend(new_links)
            start += 1
            crawl = bool(len(new_links))
        return links

    def start(self, store=False):
        all_links = {}
        for cat in self.category:
            cat_link = self.crawl_page(self.link.format(cat))
            all_links[cat] = cat_link
        if store:
            self.storing(all_links)
        return all_links

    @staticmethod
    def storing(links):
        Digiato.create_data_table()
        BaseImporter.loader(links)


class DataCrawler(CrawlerBase):
    MODEL_NAME = [Technology, Mobile, Car, Business,
                  HowStuffWorks, Science, Review]

    def __init__(self):
        self.links = self.__load_links(self.MODEL_NAME)
        self.parser = Parser()

    @staticmethod
    def __load_links(model_list):
        return Digiato.link_reader(model_list)

    def start(self, store=False):
        for link in self.links:
            response = self.get_page(link)
            print(response)


    @staticmethod
    def storing(data):
        pass


