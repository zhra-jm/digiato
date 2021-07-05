from abc import ABC, abstractmethod
from config import LINK, CATEGORY

import requests
from bs4 import BeautifulSoup

from importer import BaseImporter
from models import Digiato


class CrawlerBase(ABC):

    @abstractmethod
    def start(self):
        pass


class LinkCrawler(CrawlerBase):

    def __init__(self, category=CATEGORY, link=LINK):
        self.category = category
        self.link = link

    @staticmethod
    def get_page(link, start):
        try:
            response = requests.get(link + str(start))
        except requests.HTTPError:
            return None
        return response

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
            page = self.get_page(link, start)
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

