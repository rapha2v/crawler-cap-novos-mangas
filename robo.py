import requests
from models.robo_models import OptionsRobo


class Robo:
    def __init__(self, options: OptionsRobo):
        self.options = options
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            **self.options.headers
        }
        self.robo = requests.Session()

    def acessar(self):
        self.check_url()
        return self.robo.request(
            method='GET',
            url=self.options.url,
            headers=self.headers,
            proxies=self.get_proxie() if self.options.proxies else None,
            timeout=self.options.timeout,
            data=self.options.data,
            cookies=self.options.cookies
        )

    def check_url(self):
        if not self.options.url:
            raise Exception('URL não informada')

    @staticmethod
    def get_proxie():
        return {
            'http': "http://scraperapi:b5aee0133ff6d9662580e72b96d11e83@proxy-server.scraperapi.com:8001",
            'https': "http://scraperapi:b5aee0133ff6d9662580e72b96d11e83@proxy-server.scraperapi.com:8001"
        }

    def timeout(self):
        if self.options.timeout:
            return self.options.timeout
