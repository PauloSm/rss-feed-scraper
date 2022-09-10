from typing import Union

from system.parse_service.base_parser import BaseParser
from system.exceptions.exceptions import ParseException


class EngadgetParser(BaseParser):
    """Class used to represent the Engadget parser. Inherits from BaseParser

        Attributes:
            website_url: URL of the site to be parsed.
            rss_link_element: Name of the element containing the link to rss feed page.
            rss_link_attr_name: Name of the attribute that will serve as the unique identifier to the rss feed link.
            rss_link_attr_value: Value of the attribute that will serve as the unique identifier to the rss feed link.
    """

    def __init__(self):
        super().__init__()
        self.website_url = "https://www.engadget.com"
        self.rss_link_element = "a"
        self.rss_link_attr_name = "alt"
        self.rss_link_attr_value = "RSS Feed"

    def get_rss_link(self, page_content) -> Union[str, None]:
        """
        Parse the rss feed page and return the information.

        Args:
            page_content: Content of the page to be parsed.
        Returns:
            A string with the url to rss feed page.
        """

        soup = self.soup_constructor(page_content)
        element = soup.find(self.rss_link_element, attrs={self.rss_link_attr_name: self.rss_link_attr_value})
        if element:
            try:
                return element["href"]
            except AttributeError as error:
                raise ParseException(error)
        return None
