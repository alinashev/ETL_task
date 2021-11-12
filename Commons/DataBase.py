import psycopg2
from psycopg2 import Error

import credentials
from Logger import Logger


class DataBase:
    __connection = None

    __user = credentials.user
    __password = credentials.password
    __database = credentials.database

    @classmethod
    def connect(cls):
        if not cls.__connection:
            Logger.write_log('Establishing connection...')
            try:
                cls.__connection = psycopg2.connect(user=cls.__user,
                                                    password=cls.__password,
                                                    database=cls.__database)
            except (Exception, Error) as error:
                Logger.write_error(error)

        else:
            Logger.write_log('Connection established')
        return cls.__connection

    @classmethod
    def close(cls):
        if cls.__connection:
            Logger.write_log('Close connection')
            cls.__connection.close()
