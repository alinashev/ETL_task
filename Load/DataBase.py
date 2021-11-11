import psycopg2
from psycopg2 import Error

import credentials


class DataBase:
    __connection = None

    __user = credentials.user
    __password = credentials.password
    __database = credentials.database

    @classmethod
    def connect(cls):
        if not cls.__connection:
            print('Establishing connection...')
            try:
                cls.__connection = psycopg2.connect(user=cls.__user,
                                                    password=cls.__password,
                                                    database=cls.__database)
            except (Exception, Error) as error:
                print(error)
        else:
            print("Connection established")
        return cls.__connection
