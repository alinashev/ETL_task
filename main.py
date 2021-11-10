from Extract.Reader import Reader
from Load.loadingToDWH import LoadingToDWH
from Transform.ConvertToObjectQuestions import ConvertToObjectQuestions


def main():
    reader = Reader()
    array_json_questions = reader.open_json_file()['questions']
    load = LoadingToDWH()
    load.loadQuestions(ConvertToObjectQuestions.convert_questions(array_json_questions))


if __name__ == '__main__':
    main()
