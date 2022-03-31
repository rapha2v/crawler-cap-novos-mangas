from utils.json_serialize_deserializer import Deserializer


class OptionsRobo(Deserializer):
    def __init__(self, method: str, url: str, proxies: bool = False, headers: dict = None, timeout: int = 30000,
                 data: dict = None, cookies: dict = None):
        self.method = method
        self.url = url
        self.headers = headers
        self.timeout = timeout
        self.proxies = proxies
        self.data = data
        self.cookies = cookies
