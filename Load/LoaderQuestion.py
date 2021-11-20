import logging

from Commons.DataBase import DataBase
from Load.Loader import Loader


class LoaderQuestion(Loader):
    def loading_to_DWH(self, list_for_load):
        try:
            connect = DataBase.connect()
            cursor = connect.cursor()
            for i in list_for_load:
                questions_obj = i
                insert_query = """INSERT INTO questions (id, question, field_id) VALUES ('{id}', '{question}', 
                        '{field_id}')""".format(
                    id=questions_obj.id,
                    question=questions_obj.question,
                    field_id=questions_obj.field_id
                )
                cursor.execute(insert_query)
                connect.commit()
            logging.info('Successfully inserted')
            cursor.close()
        except Exception as error:
            logging.error(error)
