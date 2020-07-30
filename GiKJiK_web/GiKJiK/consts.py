class QuizConsts:
    NOT_OVERDUE = '0'
    OVERDUE = '1'

    states = (
        (NOT_OVERDUE, "Not Overdue"),
        (OVERDUE, "Overdue")
    )

class AnswerConsts:
    CORRECT = '0'
    WRONG = '1'
    NOT_ANSWERED = '2'

    states = (
        (CORRECT, "Correct"),
        (WRONG, "Wrong"),
        (NOT_ANSWERED, "Not Answered")
    )
