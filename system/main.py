import json
import time
import threading

from system.scrapers.verge_scraper import VergeScraper
from system.scrapers.engadget_scraper import EngadgetScraper
from system.scrapers.gizmodo_scraper import GizmodoScraper
from system.scrapers.phoronix_scraper import PhoronixScraper
from system.utils.utils import sort_dict_list_by_date


verge_scraper = VergeScraper()
engadget_scraper = EngadgetScraper()
gizmodo_scraper = GizmodoScraper()
phoronix_scraper = PhoronixScraper()


def get_pages():
    """Call the scrapers get_main_page using a multi thread approach"""

    thread1 = threading.Thread(target=verge_scraper.get_main_page)
    thread2 = threading.Thread(target=engadget_scraper.get_main_page)
    thread3 = threading.Thread(target=gizmodo_scraper.get_main_page)
    thread4 = threading.Thread(target=phoronix_scraper.get_main_page)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


def parse_rss_link():
    """Parse rss feed links"""

    verge_scraper.extract_rss_link()
    engadget_scraper.extract_rss_link()
    gizmodo_scraper.extract_rss_link()
    phoronix_scraper.extract_rss_link()


def get_rss_feed():
    """Call the scrapers get_rss_page using a multi thread approach"""

    thread1 = threading.Thread(target=verge_scraper.get_rss_page)
    thread2 = threading.Thread(target=engadget_scraper.get_rss_page)
    thread3 = threading.Thread(target=gizmodo_scraper.get_rss_page)
    thread4 = threading.Thread(target=phoronix_scraper.get_rss_page)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


def parse_rss_feed():
    """Parse rss feed pages"""

    data_list = list()
    data_list = data_list + verge_scraper.extract_data()
    data_list = data_list + engadget_scraper.extract_data()
    data_list = data_list + gizmodo_scraper.extract_data()
    data_list = data_list + phoronix_scraper.extract_data()
    save_to_json(data_list)


def save_to_json(data_list):
    """
    Sort and save the data in the json file.

    Args:
        data_list: List with the information to be saved in the file.
    """

    sort_dict_list_by_date(data_list)
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    start = time.time()
    get_pages()
    parse_rss_link()
    get_rss_feed()
    parse_rss_feed()
    end = time.time() - start
    print("Finished in: ", end)
