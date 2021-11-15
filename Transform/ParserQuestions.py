from Transform.Parser import Parser
from Entities.questions import Question


class ParserQuestions(Parser):

    def parse_to_obj(self, json_string):
        array_json = json_string['questions']
        list_of_question_obj = list()
        for i in array_json:
            list_of_question_obj.append(Question(i['id'], i['question'], i['field_id'], None))
        return list_of_question_obj
