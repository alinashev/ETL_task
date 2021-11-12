class Data:

    def __init__(self, stats, questions, responses):
        self.stats = stats
        self.questions = questions
        self.responses = responses

    def __str__(self):
        return 'stats{stats}' \
               '\nquestions{questions}' \
               '\nresponses{responses}'.format(stats=self.stats,
                                               questions=self.questions,
                                               responses=self.responses)