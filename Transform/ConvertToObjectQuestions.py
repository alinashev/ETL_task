from Entities.Questions.questions import Question
from Entities.Responses.metadata import Metadata
from Service.iterator import Iterator


class ConvertToObjectQuestions:

    @staticmethod
    def convert_questions(json_string):
        array_json = json_string['questions']
        list_of_question_obj = list()

        iterator = Iterator(array_json)
        while iterator.has_next():
            current = iterator.next()
            list_of_question_obj.append(Question(current['id'], current['question'], current['field_id'], None))
        return list_of_question_obj

    @staticmethod
    def convert_metadata(json_string):
        array_json = json_string['responses']
        list_of_metadata_obj = list()

        iterator = Iterator(array_json)
        while iterator.has_next():
            current = iterator.next()['metadata']
            list_of_metadata_obj.append(Metadata(current['browser'],
                                                 current['platform'],
                                                 current['date_land'],
                                                 current['date_submit'],
                                                 current['user_agent'],
                                                 current['referer'],
                                                 current['network_id']
                                                 ))
        return list_of_metadata_obj
