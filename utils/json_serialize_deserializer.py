from json import JSONEncoder


class Deserializer:
    def encoder(self):
        return self.__dict__


class JsonEncoder(JSONEncoder):
    def default(self, opt):
        if isinstance(opt, Deserializer):
            return opt.encoder()
        return JSONEncoder.default(self, opt)
