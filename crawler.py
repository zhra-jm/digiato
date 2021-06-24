from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class CrawlerBase(ABC):
    @abstractmethod
    def start(self):
        pass


class LinkCrawler:

    def __init__(self, category, link):
        self.category = category
        self.link = link

    def get_page(self, start):
        try:
            response = requests.get(self.link + str(start))
        except requests.HTTPError:
            return None
        return response

    @staticmethod
    def find_links(html_doc):
        tag_links = []
        soup = BeautifulSoup(html_doc, 'html.parser')
        for tag in soup.find_all('h3', attrs={'class': 'title'}):
            for a_tag in tag.find_all('a'):
                tag_links.append(a_tag['href'])
        return tag_links

    def crawl_page(self, link):
        start = 0
        links = []
        crawl = True
        while crawl:
            page = get_page(link, start)
            new_links = find_links(page.text)
            links.extend(new_links)
            start += 1
            crawl = bool(len(new_links))
        return links

    def crawl_category():
        category = ['tech', 'mobile']
        # 'car', 'business', 'howstuffworks','science', 'dgreview', 'yesterday-news', 'tablighat'
        link = "https://digiato.com/topic/{}/page/"
        all_links = {}
        for cat in category:
            cat_link = crawl_page(link.format(cat))
            all_links[cat] = cat_link
        return all_links
