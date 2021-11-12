from Commons.Convert.Convert import Convert
from Entities.Responses.metadata import Metadata


class ConvertMetadata(Convert):
    def convert_to_obj(self, json_string):
        array_json = json_string['responses']
        list_of_metadata_obj = list()
        for i in array_json:
            current = i['metadata']
            list_of_metadata_obj.append(Metadata(**current))
        return list_of_metadata_obj
