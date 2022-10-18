import requests
from pprint import pprint


class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    base_url = "https://newsapi.org/v2/everything"
    api_key = "35128dbe26e74d0a8f6459bc124c95a3"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        response = requests.get(url)
        content = response.json()

        email_body = ""
        for article in content["articles"]:
            email_body += article["title"] + "\n" + article["url"] + "\n\n"

        return email_body

    def _build_url(self):
        url = f"{self.base_url}?" \
              f"q={self.interest}&" \
              f"language={self.language}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"apiKey={self.api_key}"
        return url
