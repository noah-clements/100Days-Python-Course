class Question:

    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer

    def __repr__(self) -> str:
        return "<Question text:%s, answer:%s>" % (self.text, self.answer)
    