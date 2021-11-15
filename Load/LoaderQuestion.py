from Commons.DataBase import DataBase
from Load.Loader import Loader
from Logger import Logger


class LoaderQuestion(Loader):
    def loading_to_DWH(self, list_for_load):
        try:
            cursor = DataBase.connect().cursor()
            for i in list_for_load:
                questions_obj = i
                insert_query = """INSERT INTO questions (id, question, field_id) VALUES ('{id}', '{question}', 
                        '{field_id}')""".format(
                    id=questions_obj.id,
                    question=questions_obj.question,
                    field_id=questions_obj.field_id
                )
                cursor.execute(insert_query)
                DataBase.connect().commit()
            Logger.write_log('Successfully inserted')
            cursor.close()
        except Exception as error:
            Logger.write_error(error)