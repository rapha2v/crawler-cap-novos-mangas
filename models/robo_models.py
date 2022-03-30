from utils.json_serialize_deserializer import Deserializer


class OptionsRobo(Deserializer):
    def __init__(self, method: str, url: str, headers: dict | None, timeout: int | None,
                 proxies: bool | None, data: dict | None, cookies: dict | None):
        self.method = method
        self.url = url
        self.headers = headers
        self.timeout = timeout
        self.proxies = proxies
        self.data = data
        self.cookies = cookies
