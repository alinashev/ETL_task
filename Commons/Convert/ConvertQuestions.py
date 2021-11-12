from Commons.Convert.Convert import Convert
from Entities.Questions.questions import Question


class ConvertQuestions(Convert):

    def convert_to_obj(self,json_string):
        array_json = json_string['questions']
        list_of_question_obj = list()
        for i in array_json:
            list_of_question_obj.append(Question(i['id'], i['question'], i['field_id'], None))
        return list_of_question_obj
