from Extract.Reader import Reader
from Load.loadingToDWH import LoadingToDWH
from Transform.ConvertToObjectQuestions import ConvertToObjectQuestions


def main():
    reader = Reader()
    array_json = reader.get_json()
    LoadingToDWH.load_questions(ConvertToObjectQuestions.convert_questions(array_json))
    LoadingToDWH.load_matadata(ConvertToObjectQuestions.convert_metadata(array_json))


if __name__ == '__main__':
    main()
