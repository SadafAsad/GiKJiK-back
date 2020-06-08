class QuizConsts:
    MULTIPLE_CHOICE = '0'
    SHORT_ANSWER = '1'
    BOTH = '2'

    types = (
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (SHORT_ANSWER, "Short Answer"),
        (BOTH, "Both")
    )

class AnswerConsts:
    MULTIPLE_CHOICE = '0'
    SHORT_ANSWER = '1'

    types = (
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (SHORT_ANSWER, "Short Answer")
    )

    CORRECT = '0'
    WRONG = '1'
    NOT_ANSWERED = '2'

    states = (
        (CORRECT, "Correct"),
        (WRONG, "Wrong"),
        (NOT_ANSWERED, "Not Answered")
    )
