from Load.DataBase import DataBase


class LoadingToDWH:
    def loadQuestions(self, list_for_convert):
        print("1", list_for_convert)
        cursor = DataBase.connect().cursor()

        for i in list_for_convert:
            questions_obj = i
            insert_query = """ INSERT INTO questions (id, question, field_id) VALUES ('{id}', '{question}', '{field_id}')""".format(

                id = questions_obj.id,
                question = "none",
                field_id = questions_obj.field_id
            )
            cursor.execute(insert_query)
            DataBase.connect().commit()
            print("Successfully inserted")
