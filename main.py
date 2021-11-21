import datetime
import logging

from Commons.StorageS3 import StorageS3
from Transform.ParserMetadata import ParserMetadata
from Transform.ParserQuestions import ParserQuestions
from Commons.ReaderJSON import ReaderJSON
from Commons.DataBase import DataBase
from Load.LoaderMetadata import LoaderMetadata
from Load.LoaderQuestion import LoaderQuestion


def main():
    time = datetime.datetime.utcnow()
    log_file_name = '{year}-{month}-{day}UTC{hour}-{minute}-{second}.log'.format(year=time.year,
                                                                               month=time.month,
                                                                               day=time.day,
                                                                               hour=time.hour,
                                                                               minute=time.minute,
                                                                               second=time.second)

    logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    storage = StorageS3()
    storage.download_folder('Resources')

    reader = ReaderJSON(storage.get_path())
    array_json = reader.get_json()

    LoaderQuestion().loading_to_DWH(ParserQuestions().parse_to_obj(array_json))
    LoaderMetadata().loading_to_DWH(ParserMetadata().parse_to_obj(array_json))

    DataBase.close()
    storage.load_logs_to_s3(log_file_name)


if __name__ == '__main__':
    main()
