from Transform.Parser import Parser
from Entities.metadata import Metadata


class ParserMetadata(Parser):
    def parse_to_obj(self, json_string):
        return (Metadata(**i['metadata']) for i in json_string['responses'])
