import requests
from models.robo_models import OptionsRobo


class Robo:
    def __init__(self, options: OptionsRobo):
        self.options = options
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        self.proxy_server = "http://api.scraperapi.com/?api_key=<YOUR_KEY>&url="
        self.robo = requests.Session()

    def acessar(self):
        response = self.make_request()
        return {
            'content': response.text,
            'headers': response.headers,
            'cookies': response.cookies,
            'status': response.status_code,
        }

    def make_request(self):
        self.check_url()
        self.add_header()
        return self.robo.request(
            method=self.options.method if self.options.method else 'GET',
            url=self.options.url,
            headers=self.headers,
            proxies=self.proxy_server if self.options.proxies else None,
            timeout=self.options.timeout,
            data=self.options.data,
            cookies=self.options.cookies
        )

    def check_url(self):
        if not self.options.url:
            raise Exception('URL não informada.')

    def add_header(self):
        if self.options.headers:
            self.headers += self.options.headers

    def timeout(self):
        if self.options.timeout:
            return self.options.timeout


opt = OptionsRobo('GET', 'https://neoxscans.net/', False)
c = Robo(opt)
print(c.acessar())
