from Transform.Parser import Parser
from Entities.metadata import Metadata


class ParserMetadata(Parser):
    def parse_to_obj(self, json_string):
        array_json = json_string['responses']
        list_of_metadata_obj = list()
        for i in array_json:
            current = i['metadata']
            list_of_metadata_obj.append(Metadata(**current))
        return list_of_metadata_obj
