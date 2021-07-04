import sys
from crawler import LinkCrawler
from models import Digiato
from importer import BaseImporter

if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == 'find_and_store_links':
        link_crawler = LinkCrawler()
        links = link_crawler.start()
        Digiato.create_data_table()
        BaseImporter.loader(links)






