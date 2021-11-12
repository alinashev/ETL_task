class Responses:

    def __init__(self, completed, token, metadata, hidden, answers):
        self.completed =completed
        self.token = token
        self.metadata = metadata,
        self.hidden = hidden
        self.answers = answers

    def __str__(self):
        return 'completed{completed}' \
               '\ntoken{token}' \
               '\nmetadata{metadata}' \
               '\nhidden{hidden}' \
               '\nanswers{answers}'.format(completed=self.completed,
                                           token=self.token,
                                           metadata=self.metadata,
                                           hidden=self.hidden,
                                           answers=self.answers)
