from typing import Union

from bs4 import BeautifulSoup

from system.exceptions.exceptions import ParseException
from system.utils.utils import format_date


class BaseParser:
    """Generic class used to represent a parser.

        Attributes:
            title: Article title of the extracted element.
            publication_date: Article publication date of the extracted element.
            link: Publication Article link of the extracted element.
    """

    def __init__(self):
        self.title = None
        self.publication_date = None
        self.link = None

    def soup_constructor(self, page_content: bytes, parser: str = "html.parser") -> BeautifulSoup:
        """
        Instantiates a BeautifulSoup object with the page to be parsed.

        Args:
            page_content: Content of the page to be parsed.
            parser: The type of parser. It can be html.parser or xml.
        Returns:
            A BeautifulSoup object
        """
        return BeautifulSoup(page_content, parser)

    def _get_main_entity(self, page_content: bytes, entity: str) -> Union[list, None]:
        """
        Gets the first ten elements that contains the information about a post.

        Args:
            page_content: Content of the page to be parsed.
            entity: Element name.
        Returns:
            A list of the first ten elements.
        """

        soup = self.soup_constructor(page_content, "xml")
        entries = soup.findAll(entity, limit=10)
        if len(entries) > 0:
            return entries
        return None

    def get_attributes(self, page_content: bytes, main_entity: str, title: str, pub_date: str, link: str):
        """
        Get the article information in the main element (captured by _get_main_entity).

        Args:
            page_content: Content of the page to be parsed.
            main_entity: Element name.
            title: Name of the element containing the title.
            pub_date: Name of the element containing the publication date.
            link: Name of the element containing the link to the article.
        Returns:
            A list of information (title, pub_date, link) about the first ten entries.
        """

        entries = self._get_main_entity(page_content, main_entity)
        data_list = list()
        for entry in entries:
            try:
                self.title = entry.find(title).text
                self.publication_date = format_date(entry.find(pub_date).text)
                self.link = entry.find(link).text
            except AttributeError as error:
                raise ParseException(error)
            data_list.append({"title": self.title, "date": self.publication_date, "link": self.link})
        return data_list

    def get_rss_link(self, page_content: bytes) -> str:
        """
        Get the url to rss feed page.

        Args:
            page_content: Content of the page to be parsed.
        Returns:
            A string with the url to rss feed page.
        """

        return str()
