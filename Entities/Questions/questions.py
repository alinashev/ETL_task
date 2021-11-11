class Question:
    id = None
    question = None
    field_id = None
    group = None

    def __init__(self, id, question, field_id, group):
        self.id = id
        self.question = question
        self.field_id = field_id
        self.group = group

    def __str__(self):
        return 'id{id} ' \
               '\nquestion{question} ' \
               '\nfield_id{field_id}'.format(id=self.id,
                                             question=self.question,
                                             field_id=self.field_id)
