from Transform.ParserMetadata import ParserMetadata
from Transform.ParserQuestions import ParserQuestions
from Commons.ReaderJSON import ReaderJSON
from Commons.DataBase import DataBase
from Load.LoaderMetadata import LoaderMetadata
from Load.LoaderQuestion import LoaderQuestion


def main():
    reader = ReaderJSON('Resources/Lake/jsonTypesFile/osmi.json')
    array_json = reader.get_json()
    LoaderQuestion().loading_to_DWH(ParserQuestions().parse_to_obj(array_json))
    LoaderMetadata().loading_to_DWH(ParserMetadata().parse_to_obj(array_json))
    DataBase.close()


if __name__ == '__main__':
    main()
