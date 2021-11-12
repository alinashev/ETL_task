import json

import settings


class Reader:
    __path = settings.path

    def open_json_file(self):
        with open(self.__path, 'r', encoding='utf-8') as f:
            self.text = json.load(f)
        return self.text

    def get_json(self):
        return Reader.open_json_file(self)
