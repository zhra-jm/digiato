import sys
from crawler import LinkCrawler, DataCrawler
from models import Digiato, Car, Mobile

if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == 'find_and_store_links':
        link_crawler = LinkCrawler()
        link_crawler.start(store=True)
    elif switch == "read_links":
        data_crawler = DataCrawler()
        data_crawler.start()






