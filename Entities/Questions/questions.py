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

    def __str__(self) :
        print(" id: ", self.id, "\n",
              "qestion: ", self.question, "\n",
              "field_id: ", self.field_id, "\n",
              "group: ", self.group, "\n")
