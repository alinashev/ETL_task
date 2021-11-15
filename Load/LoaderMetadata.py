from Commons.DataBase import DataBase
from Load.Loader import Loader
from Logger import Logger


class LoaderMetadata(Loader):
    def loading_to_DWH(self, list_for_load):
        try:
            cursor = DataBase.connect().cursor()

            for i in list_for_load:
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
            Logger.write_log('Successfully inserted')
        except Exception as error:
            Logger.write_error(error)
