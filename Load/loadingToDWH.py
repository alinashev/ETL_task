from Load.DataBase import DataBase


class LoadingToDWH:
    @staticmethod
    def load_questions(list_for_convert):
        cursor = DataBase.connect().cursor()

        for i in list_for_convert:
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

    @staticmethod
    def load_matadata(list_for_convert):
        cursor = DataBase.connect().cursor()

        for i in list_for_convert:
            metadata_obj = i
            insert_query = """INSERT INTO metadata (browser, platform, date_land, date_submit, user_agent, referer, 
            network_id) VALUES ('{browser}', '{platform}', '{date_land}', '{date_submit}', '{user_agent}', 
            '{referer}', '{network_id}') """.format(
                browser=metadata_obj.browser,
                platform=metadata_obj.platform,
                date_land=metadata_obj.date_land,
                date_submit=metadata_obj.date_submit,
                user_agent=metadata_obj.user_agent,
                referer=metadata_obj.referer,
                network_id=metadata_obj.network_id
            )

            cursor.execute(insert_query)
            DataBase.connect().commit()
        print("Successfully inserted")
