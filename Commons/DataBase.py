import logging
import psycopg2
from psycopg2 import Error
import settings


class DataBase:
    __connection = None

    __user = settings.user
    __password = settings.password
    __database = settings.database
    __host = settings.host
    __port = settings.port

    @classmethod
    def connect(cls):
        if not cls.__connection:
            logging.info('Establishing connection...')
            try:
                cls.__connection = psycopg2.connect(user=cls.__user,
                                                    password=cls.__password,
                                                    database=cls.__database,
                                                    host=cls.__host,
                                                    port=cls.__port)
            except (Exception, Error) as error:
                logging.error(error)

        else:
            logging.info('Connection established')
        return cls.__connection

    @classmethod
    def close(cls):
        if cls.__connection:
            logging.info('Close connection')
            cls.__connection.close()
