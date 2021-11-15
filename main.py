from Transform.ConvertMetadata import ConvertMetadata
from Transform.ConvertQuestions import ConvertQuestions
from Commons.ReaderJSON import ReaderJSON
from Commons.DataBase import DataBase
from Load.LoadingMetadata import LoadingMetadata
from Load.LoadingQuestion import LoadingQuestion


def main():
    reader = ReaderJSON('Resources/Lake/jsonTypesFile/osmi.json')
    array_json = reader.get_json()
    LoadingQuestion().loading_to_DWH(ConvertQuestions().convert_to_obj(array_json))
    LoadingMetadata().loading_to_DWH(ConvertMetadata().convert_to_obj(array_json))
    DataBase.close()


if __name__ == '__main__':
    main()
