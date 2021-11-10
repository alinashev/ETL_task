from Entities.Questions.questions import Question


class ConvertToObjectQuestions:
    @staticmethod
    def convert_questions(arrayJson):  #return list with questions-entities objects
        list_of_question_obj = list()
        iterator = iter(arrayJson)
        has_next = True
        while has_next:
            try:
                current = next(iterator)
                list_of_question_obj.append(Question(current['id'], current['question'], current['field_id'], None))
            except StopIteration:
                has_next = False
        return list_of_question_obj
