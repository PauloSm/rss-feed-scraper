import requests

from system.exceptions.exceptions import HTTPBaseException


class BaseRequest:
    """Class used to represent HTTP requests."""

    @staticmethod
    def get_page(url: str) -> bytes:
        """
        Do a HTTP Get request to a url.

        Args:
            url: uniform resource locator of the required page.
        Returns:
            Content of the response in bytes.
        """

        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPBaseException(status_code=response.status_code, url=url)
        return response.content
