from system.request_service.base_request import BaseRequest
from system.parse_service.gizmodo_parse import GizmodoParser


class GizmodoScraper:
    """
    Class used to represent the Gizmodo scraper.

    Attributes:
        url: URL of the website.
        html_page: Website html page content in bytes.
        rss_link: URL of the rss feed page.
        rss_page: Content of the rss feed page in bytes.
        parser: Instance of EngadgetParser.
        main_element: Name of the element that contains the information about a post.
        title: Name of the element that contains the title.
        pub_date: Name of the element that contains the publication date.
        link: Name of the element that contains the link to the post.
    """

    def __init__(self):
        self.url = "https://es.gizmodo.com"
        self.html_page = bytes()
        self.rss_link = str()
        self.rss_page = bytes()
        self.parser = GizmodoParser()
        self.main_element = "item"
        self.title = "title"
        self.pub_date = "pubDate"
        self.link = "link"

    def get_main_page(self):
        """Request the website page and assigns the content to the html_page attribute."""

        self.html_page = BaseRequest.get_page(self.url)

    def extract_rss_link(self):
        """Parse the rss link and assigns the content to the rss_link attribute."""

        self.rss_link = self.parser.get_rss_link(self.html_page)

    def get_rss_page(self):
        """Request the rss feed page and assigns the content to the rss_page attribute."""

        self.rss_page = BaseRequest.get_page(self.rss_link)

    def extract_data(self):
        """
        Parse the rss feed page and return the information.

        Returns:
            A list of information (title, pub_date, link) about the first ten entries.
        """

        return self.parser.get_attributes(self.rss_page, self.main_element, self.title, self.pub_date, self.link)


if __name__ == '__main__':
    scraper = GizmodoScraper()
    scraper.get_main_page()
    scraper.extract_rss_link()
    scraper.get_rss_page()
    print(scraper.extract_data())
