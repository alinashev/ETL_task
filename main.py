from Commons.Convert.ConvertMetadata import ConvertMetadata
from Commons.Convert.ConvertQuestions import ConvertQuestions
from Commons.Reader import Reader
from Commons.DataBase import DataBase
from Load.LoadingMetadata import LoadingMetadata
from Load.LoadingQuestion import LoadingQuestion


def main():
    reader = Reader()
    array_json = reader.get_json()
    LoadingQuestion().loading_to_DWH(ConvertQuestions().convert_to_obj(array_json))
    LoadingMetadata().loading_to_DWH(ConvertMetadata().convert_to_obj(array_json))
    DataBase.close()


if __name__ == '__main__':
    main()
