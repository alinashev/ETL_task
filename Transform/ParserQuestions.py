from Transform.Parser import Parser
from Entities.questions import Question


class ParserQuestions(Parser):

    def parse_to_obj(self, json_string):
        return (Question(i['id'], i['question'], i['field_id'], None) for i in json_string['questions'])
