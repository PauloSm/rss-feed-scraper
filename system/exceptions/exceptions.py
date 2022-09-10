import logging
from typing import Union

logging.basicConfig(filename="scraper-exceptions.log", level=logging.ERROR)


class HTTPBaseException(Exception):
    """Generic class used to represent exceptions caused by HTTP errors.

        Attributes:
            status_code: Status code generated by the HTTP request.
            url: URL requested.
    """

    def __init__(self, status_code: int = 500, url: str = None) -> None:
        self.status_code = status_code
        self.url = url
        if self.url:
            logging.error(f"HTTP {self.status_code} status code on request {self.url}")


class ParseException(Exception):
    """Generic class used to represent exceptions caused by the parsing process.

        Attributes:
            message: Error message detailing the error.
    """

    def __init__(self, message: Union[str, AttributeError]):
        self.message = message
        logging.error(self.message)

