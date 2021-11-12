from Commons.DataBase import DataBase
from Load.Loading import Loading


class LoadingQuestion(Loading):
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
            print("Successfully inserted")
            cursor.close()
        except Exception as error:
            print(error)